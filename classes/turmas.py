from classes.timetable import *

class classes():
    
    def __init__(self, classname):
        self.classname = classname

        self.schedule = WeekSchedule(classname)
        #self.edit_day()

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

        input("Press enter to continue.")

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
    
    def undo(self):
        """
        Escolhe o dia para desfazer alteração de horário.
        """
        while True:
            choice = str(input('Choose the day or 0 for quit: ')).lower()
            if choice == '0':
                break
            self.schedule.undo(choice)

    def add_student(self, student_name):
        self.students.append(student_name)

    def add_exams(self, exams_matter, date):
        self.exams[exams_matter] = date

"""
padrão composite, antes os dias eram tratados separadamente em 'classes' de maneira semelhante, portanto foi adicionado esse padrão
para melhorar o funcionamento e manutenção, caso seja nescessário adicionar um novo dia como sábado por exemplo ou adicionar novas funcionalidades aos dias.
"""
class WeekSchedule:
    def __init__(self, classname):
        self.classname = classname
        self.days ={
            'monday': Timetable('Monday', 'vague', 'vague', 'vague', 'vague', 'vague'),
            'tuesday': Timetable('Tuesday', 'vague', 'vague', 'vague', 'vague', 'vague'),
            'wednesday': Timetable('Wednesday', 'vague', 'vague', 'vague', 'vague', 'vague'),
            'thursday': Timetable('Thursday', 'vague', 'vague', 'vague', 'vague', 'vague'),
            'friday': Timetable('Friday', 'vague', 'vague', 'vague', 'vague', 'vague')
        }

    def show_all(self):
        for day in self.days.values():
            day.show(self.classname)

    def edit_day(self, day_name):
        day = self.days.get(day_name.lower())
        if not day:
            print("Invalid day or day name.")
            return
        
        while True:
            day.show(self.classname)
            time = input('Choose the time or 0 to quit: ')
            if time == '0':
                break
            day.edit(time.lower())
    
    def undo(self, day_name):
        day = self.days.get(day_name.lower())
        if not day:
            print("Invalid day or day name.")
            return
        
        day.show(self.classname)
        day.undo()
