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
        self.editor = Editor()

    def show(self, classname):
        print(f"{classname}: {self.day}")
        for time, subject in self.schedule.items():
            print(f"{time.capitalize()}: {subject}")
    
    def update(self, time, subject):
        if time in self.schedule:
            old_subject = self.schedule[time]
            self.schedule[time] = subject
            input(f"{time} updated from {old_subject} to {subject}. Press enter to continue.")
        else:
            input(f"Invalid {time}. Press enter to continue.")

    def edit(self, time):
        cmd = Edit_Time_Command(self, time)
        self.editor.execute_command(cmd)
    
    def undo(self):
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
    def __init__(self, timetable, time):
        self.timetable = timetable
        self.time = time
    
    def execute(self):
        current_subject = self.timetable.schedule.get(self.time)
        if current_subject is None:
            input(f"Invalid time slot: {self.time}, press enter to continue.")
        else:
            print(f"Current subject at {self.time} is: {current_subject}")
            opt = int(input("0 - return\n1 - edit"))
            if opt == 1:
                new_subject = input("Enter a new subject: ")
                self.timetable.update(self.time, new_subject)
            else:
                input("Operation cancelled. Press enter to continue.")

    def undo(self):
        if self.previous_subject is not None:
            self.timetable.update(self.time, self.previous_subject)
            input(f"Undo complete. Restored {self.time} to {self.previous_subject}. Press enter to continue.")
        else:
            input("Nothing to undo. Press enter to continue.")

class Editor():
    def __init__(self):
        self.history = []

    def execute_command(self, command: Command):
        command.execute()
        self.history.append(command)
    
    def undo_last(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
        else:
            input("No actions to undo. Press enter to continue.")

