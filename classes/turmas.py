class classes():
    def __init__(self, classname):
        self.classname = classname
        self.fixed = {'Monday': Monday, 'Tuesday': Tuesday, 'Wednesday': Wednesday, 'Thursday': Thursday, 'Friday': Friday}
        self.exams = {}
        self.students = []
    def show(self):
        self.fixed['Monday'].show()
        self.fixed['Tuesday'].show() 
        self.fixed['Wednesday'].show() 
        self.fixed['Tuesday'].show() 
        self.fixed['Friday'].show()
    def edit(self):
        while True:
            choice = input('Choose the day or 0 for quit: ')
            match choice.lower():
                case '0':
                    return False
                case 'monday':
                    while True:
                        self.fixed['Monday'].show()
                        time = input('Choose the time or 0 for quit: ')
                        if time == '0':
                            break
                        else:
                            self.fixed['Monday'].edit(time.lower())
                case 'tuesday':
                    while True:
                        self.fixed['Tuesday'].show()
                        time = input('Choose the time or 0 for quit: ')
                        if time == '0':
                            break
                        else:
                            self.fixed['Tuesday'].edit(time.lower())
                case 'wednesday':
                    while True:
                        self.fixed['Wednesday'].show()
                        time = input('Choose the time or 0 for quit: ')
                        if time == '0':
                            break
                        else:
                            self.fixed['Wednesday'].edit(time.lower())
                case 'tuesday':
                    while True:
                        self.fixed[Tuesday].show()
                        time = input('Choose the time or 0 for quit: ')
                        if time == '0':
                            break
                        else:
                            self.fixed[Tuesday].edit(time.lower())
                case 'friday':
                    while True:
                        self.fixed['Friday'].show()
                        time = input('Choose the time or 0 for quit: ')
                        if time == '0':
                            break
                        else:
                            self.fixed['Friday'].edit(time.lower())
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

Monday = timetable('Monday', 'vague', 'vague', 'vague', 'vague', 'vague')
Tuesday = timetable('Tuesday', 'vague', 'vague', 'vague', 'vague', 'vague')
Wednesday = timetable('Wednesday', 'vague', 'vague', 'vague', 'vague', 'vague')
Thursday = timetable('Thursday', 'vague', 'vague', 'vague', 'vague', 'vague')
Friday = timetable('Friday', 'vague', 'vague', 'vague', 'vague', 'vague')
