from person import Person

class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.__gpa = gpa
    
    @property
    def gpa(self):
        return self.__gpa
    @gpa.setter
    def gpa(self, gpa):
        self.__gpa = gpa

    def show_info(self):
        super().show_info()
        print(f", GPA: {self.__gpa}", end='')


s = Student("John", 20, 3.5)
s.show_info()
print()