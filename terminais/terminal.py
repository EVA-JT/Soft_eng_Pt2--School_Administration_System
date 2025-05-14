from users.final import *
from classes.turmas import *
from dados.dados import *
import os

# --- Dados ---
for user_id, user_data in users.items():
    tipo, nome, senha, *args = user_data
    users_bank[nome] = Factory.meet_the_constructor(tipo, nome, senha, *args)

users_bank['joao'].add_note('math')

for class_id, class_data in turmas.items():
    classname = class_data
    classes_bank[classname] = classes(classname)
    
classes_bank['5th grade'].add_student(users_bank['joao'].name)
classes_bank['5th grade'].add_student(users_bank['arthur'].name)
# ---

def authenticate(user_dict, username, password):
    """
    Faz o login do cliente, podendo ser um estudante ou tutor.
    """
    user = user_dict.get(username)
    if user:
        user_type = type(user).__name__  # Pega a classe do usuário
        if user.login(password):
            print(f" {username} (Type: {user_type}) has succesfully logged in!\n")
            return user_type
        else:
            print(f" {username} (Type: {user_type}) tried to log in, but the password is incorrect!.\n")
            return None
    print("User not found!\n")
    return None

class terminal:
    def __init__(self):
        pass  # Inicializa sem estudante logado

    def clear(self):
        """Escolhe qual comando usar e limpa a tela."""
        os.system("cls" if os.name == "nt" else "clear")

    def run(self):
        """Executa o loop principal do sistema."""
        while True:
            if not self.portal():
                break

    def portal(self):
        """Dá o prompt para o login e leva o usuário para o portal de estudante ou tutor."""
        while True:
            self.clear()
            name_user = input('Name: ')
            password_user = input('Password: ')

            if authenticate(users_bank, name_user, password_user) == None: #Se o login falhar, dá o prompt para fechar o programa
                choice = input('quit?(y/n) ')
                match choice.lower():
                    case 'y':
                        return False
                    case 'n':
                        pass
        
            #O usuario pode ser levado a dois tipos de portais diferentes, dependendo do tipo.
            elif authenticate(users_bank, name_user, password_user) == 'tutor':
                self.clear()
                self.tutor()

            elif authenticate(users_bank, name_user, password_user) == 'student':
                self.clear()
                self.student(users_bank[name_user].name)

# -----------------Tutor portal-----------------
    def tutor(self):
        while True:
            self.clear()
            print("Hello, what would you like to do?")
            print("0 - Quit")
            print("1 - Enroll students") #cadastra estudantes
            print('2 - Daily attendance') #presença
            print('3 - Create a class') #cria uma turma
            print('4 - Timetable manager') #altera os horários de um dia
            print('5 - Add exam') #adiciona uma prova <---------------------REVER
            print('6 - Add subject in gradebook') #adiciona uma matéria no boletim de um aluno
            print('7 - Edit gradebook') #altera a nota no boletim do aluno.
            print('8 - Create a new extra class.') #cria uma turma extra-curricular
            print('9 - Assign a student to a new extra class.') #coloca um aluno em uma turma extra-curricular
            print("10 - Show class information.")

            choice = input('action: ')
            match choice:
                case '0': # Sai do menu tutor e volta ao portal
                    return False
            
                case '1': #cadastro de estudantes
                    self.clear()
                    self.enroll_students()

                case '2': #presença
                    self.clear()
                    self.attendance()

                case '3': #criação de turma
                    self.clear()
                    self.create_class()

                case '4': #altera os horários de um dia
                    self.clear()
                    class_name = input('Class name: ')
                    opt = int(input("Extra(1) or Normal(2) class?\n"))
                    action = int(input("Edit(1) or Undo a edit(2)?\n"))
                    if opt == 1:
                        if action == 1:
                            extra_classes_bank[class_name].edit_day()
                        elif action == 2:
                            extra_classes_bank[class_name].undo()
                    elif opt == 2:
                        if action == 1:
                            classes_bank[class_name].edit_day()
                        elif action == 2:
                            classes_bank[class_name].undo()
            
                case '5': #adiciona uma prova
                    self.clear()
                    class_name = input('Class name: ')
                    if class_name not in classes_bank:
                        input("Invalid class name. Press enter to continue.")
                    else:
                        exam_matter = input('Exam matter: ')
                        exam_date = input('Exam date: ')
                        classes_bank[class_name].add_exams(exam_matter, exam_date)

                case '6': #adiciona uma matéria no boletim de um aluno
                    self.clear()
                    student_name = input('Student name:')
                    matter_name = input('Matter name: ')
                    users_bank[student_name].add_note(matter_name)
                
                case '7': #altera a nota no boletim do aluno.
                    self.clear()
                    student_name = input('Student name:')
                    matter_name = input('Matter name: ')
                    users_bank[student_name].edit_note(matter_name)
            
                case '8': #cria uma turma extra-curricular
                    name_extra_class = input('Name extra class: ')
                    new_class = classes(name_extra_class)
                    extra_classes_bank[name_extra_class] = new_class
            
                case '9': #coloca um aluno em uma turma extra-curricular
                    name_extra_class = input('Name extra class: ')
                    if name_extra_class in extra_classes_bank:
                        student_name = input('Student name: ')
                        if student_name in users_bank:
                            extra_classes_bank[name_extra_class].add_student(student_name)
                        else:
                            input('Student not found. Press enter to continue')
                    else:
                        print('Class not found. Press enter to continue')
                
                case '10': #printa as informações de uma turma
                    self.clear()
                    class_name = input('Class name: ')
                    opt = int(input("Extra(1) or Normal(2) class?\n"))
                    if opt == 1:
                        extra_classes_bank[class_name].show()
                    elif opt == 2:
                        classes_bank[class_name].show()

                case _:
                    self.clear()
                    print('Invalid option')

    def enroll_students(self):
        """
        Cadastro de estudantes.
        """
        new_name = input(f"Student's name: ")
        while True: #procura a turma para cadastra-lo
            new_classe = input('Class: ')
            if new_classe in classes_bank:
                break
            else:
                print('Class not found')
    
        new_installments = int(input('installments paid: ')) #parcelas já pagas
        new_password = '0000' #senha padrão
        new_student = student(new_name, new_password, 0, new_classe, 12 - new_installments)
        users_bank[new_name] = new_student
        classes_bank[new_classe].add_student(new_name)
        new_student.show()

    def attendance(self):
        """
        Presença. Mostra o nome da turma, os alunos e vai iterando cada um.
        """
        name_class = input('Name class: ')

        if name_class not in classes_bank:
            print("Class not found!")
            return

        print(classes_bank[name_class].students)

        for student_name in classes_bank[name_class].students:  # Iterando diretamente sobre nomes dos alunos
            print(users_bank[student_name].name)
            absence = input('Present? yes(1) or no (0)? ')
            users_bank[student_name].daily_attendance(absence)

    def create_class(self):
        """
        Criação de uma turma.
        """
        new_classename = input('Class name: ')
        new_classe = classes(new_classename)
        classes_bank[new_classename] = new_classe

# ----------------Student portal----------------
    def student(self, code):
        while True:
            print("Hello, what would you like to do?")
            print('0 - Quit')
            print("1 - See student's informations") #mostra as informações do aluno.
            print("2 - See classes' information.")
            print('3 - See gradebook') #mostra o boletim
            print('4 - Edit password') #altera a senha

            choice = input('action: ')
            self.clear()
            match choice:
                case '0': # Sai do menu aluno e volta ao portal
                    break
            
                case '1': #mostra as informações do aluno.
                    users_bank[code].show()
                case '2':
                    self.clear()
                    class_name = input('Class name: ')
                    opt = int(input("Extra(1) or Normal(2) class?\n"))
                    if opt == 1:
                        extra_classes_bank[class_name].show()
                    elif opt == 2:
                        classes_bank[class_name].show()

                case '3': #mostra o boletim
                    users_bank[code].show_note()
            
                case '4': #altera a senha
                    new_password = input('New password: ')
                    users_bank[code].edit_password(new_password)
            
                case _:
                    print('Invalid option')
