class Student:
    def __init__(self, name, id, gpa):
        self.name = name
        self.id = id
        self.gpa = gpa

    def show_info(self):
        print("Name: ", self.name)
        print("ID: ", self.id)
        print("GPA: ", self.gpa)