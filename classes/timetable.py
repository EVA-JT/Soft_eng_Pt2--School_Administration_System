from abc import ABCMeta, abstractmethod

class Timetable:
    def __init__(self, day, first, second, third, fourth, fifth):
        self.day = day
        self.schedule = {
            'first': first,
            'second': second,
            'third': third,
            'fourth': fourth,
            'fifth': fifth
        }
        self.editor = Editor() #cria um editor para cuidar dos comandos edit e undo

    def show(self, classname):
        """
        Printa a turma, dia e em seguida os horários no dia.
        """
        print(f"{classname}: {self.day}")
        for time, subject in self.schedule.items():
            print(f"{time.capitalize()}: {subject}")
        print()
    
    def update(self, time, subject):
        """
        Atualiza um horário especifico.
        """
        if time in self.schedule:
            old_subject = self.schedule[time]
            self.schedule[time] = subject
            input(f"{time.capitalize()} updated from '{old_subject}' to '{subject}'. Press enter to continue.")
        else:
            input(f"Invalid {time}. Press enter to continue.")

    def edit(self, time):
        """
        Cria um comando e o usa para fazer uma atualização em um tempo especifico.
        """
        cmd = Edit_Time_Command(self, time)
        self.editor.execute_command(cmd)
    
    def undo(self):
        """
        Desfaz a ultima atualização do dia.
        """
        self.editor.undo_last()

"""
A seguir tem uma implementação do padrão comportamental Command.
"""

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class Edit_Time_Command(Command):
    """
    Classe para o comando de edições.
    """
    def __init__(self, timetable, time):
        self.timetable = timetable
        self.time = time
        self.previous_subject = [] #lista com as matérias passadas
    
    def execute(self):
        current_subject = self.timetable.schedule.get(self.time) #pega a matéria atual
        if current_subject is None: #se falhar é porque o tempo foi digitado errado
            input(f"Invalid time slot: {self.time}, press enter to continue.")
        else:
            print(f"Current subject at {self.time} is: {current_subject}")
            opt = int(input("0 - return\n1 - edit\n"))
            if opt == 1:
                new_subject = input("Enter a new subject: ")
                self.previous_subject.append(current_subject) #salva a matéria antes da edição
                self.timetable.update(self.time, new_subject)
            else:
                input("Operation cancelled. Press enter to continue.")

    def undo(self):
        if self.previous_subject: #se houver alguma matéria na lista
            last_subject = self.previous_subject.pop()
            self.timetable.update(self.time, last_subject)
            input(f"Undo complete. Restored {self.time} to {last_subject}. Press enter to continue.")
        else:
            input("Nothing to undo. Press enter to continue.")

class Editor():
    def __init__(self):
        self.history = [] #lista com os comandos usados antes para undo_last()

    def execute_command(self, command: Command): #executa o comando dado nos parâmetros
        command.execute()
        self.history.append(command)
    
    def undo_last(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
        else:
            input("No actions to undo. Press enter to continue.")

