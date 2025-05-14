from timetable import *

class classes():
    
    def __init__(self, classname):
        self.classname = classname

        self.schedule = WeekSchedule()
        self.edit_day()

        self.exams = {}
        self.students = []

    def show(self):
        """
        Printa as informações da turma.
        """
        print(f"{self.classname}")
        print(f"Students: {self.students}")
        print(f"Exams: {self.exams}")
        self.schedule.show_all()

    def show_schedule(self):
        """
        Printa os horários da turma
        """
        self.schedule.show_all()

    def edit_day(self):
        """
        Escolhe o dia para uma alteração de horário.
        """
        while True:
            choice = str(input('Choose the day or 0 for quit: ')).lower()
            if choice == '0':
                break
            self.schedule.edit_day(choice)

    def add_student(self, student_name):
        self.students.append(student_name)

    def add_exams(self, exams_matter, date):
        self.exams[exams_matter] = date

class timetable:
    def __init__(self, day, first, second, third, fourth, fifth):
        self.day = day
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth
    
    def edit(self, time):
        if time == 'first':
            print()
            print(f'current: {self.first}')
            print('Press 0 for keep')
            print('Press 1 for edit')
            case = input('action: ')
            
            if case == '1':
                print()
                new_matter = input('New matter: ')
                self.first = new_matter
            elif case == '0':
                return 0
        elif time == 'second':
            print()
            print(f'current: {self.second}')
            print('Press 0 for edit')
            print('Press 1 for keep')
            case = input('action: ')
            
            if case == '0':
                print()
                new_matter = input('New matter: ')
                self.second = new_matter
            elif case == '1':
                return 0
        elif time == 'third':
            print()
            print(f'current: {self.third}')
            print('Press 0 for edit')
            print('Press 1 for keep')
            case = input('action: ')
            
            if case == '0':
                print()
                new_matter = input('New matter: ')
                self.third = new_matter
            elif case == '1':
                return 0
        elif time == 'fourth':
            print()
            print(f'current: {self.fourth}')
            print('Press 0 for edit')
            print('Press 1 for keep')
            case = input('action: ')
            
            if case == '0':
                print()
                new_matter = input('New matter: ')
                self.fourth = new_matter
            elif case == '1':
                return 0
        elif time == 'fifth':
            print()
            print(f'current: {self.fifth}')
            print('Press 0 for edit')
            print('Press 1 for keep')
            case = input('action: ')
            
            if case == '0':
                print()
                new_matter = input('New matter: ')
                self.fifth = new_matter
            elif case == '1':
                return 0
    def show(self):
        print()
        print(f'class: {self.day}')
        print(f'First: {self.first}')
        print(f'Second: {self.second}')
        print(f'Third: {self.third}')
        print(f'Fourth: {self.fourth}')
        print(f'Fifth: {self.fifth}')   


#padrão composite, antes os dias eram tratados separadamente em 'classes' de maneira semelhante, portanto foi adicionado esse padrão
#para melhorar o funcionamento e manutenção, caso seja nescessário adicionar um novo dia como sábado por exemplo ou adicionar novas funcionalidades aos dias.
class WeekSchedule:
    def __init__(self):
        self.days ={
            'monday': timetable('Monday', 'vague', 'vague', 'vague', 'vague', 'vague'),
            'tuesday': timetable('Tuesday', 'vague', 'vague', 'vague', 'vague', 'vague'),
            'wednesday': timetable('Wednesday', 'vague', 'vague', 'vague', 'vague', 'vague'),
            'thursday': timetable('Thursday', 'vague', 'vague', 'vague', 'vague', 'vague'),
            'friday': timetable('Friday', 'vague', 'vague', 'vague', 'vague', 'vague')
        }

    def show_all(self):
        for day in self.days.values():
            day.show()
    def edit_day(self, day_name):
        day = self.days.get(day_name.lower())
        if not day:
            print("Invalid day or day name.")
            return
        
        while True:
            day.show()
            time = input('Choose the time or 0 to quit: ')
            if time == '0':
                break
            day.edit(time.lower())
