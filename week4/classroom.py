class ClassRoom:
    def __init__(self):
        self.students = []
    
    def add(self, s):
        self.students.append(s)
        print(f'Student {s.name} is added to the class')
    
    def remove(self, id):
        for s in self.students:
            if s.id == id:
                self.students.remove(s)
                print(f'Student ID {s.id} is removed from the class')
                return
        print(f'Student with id {id} is not found')
    
    def find_best(self):
        if len(self.students) == 0:
            print('No student in the class')
            return None
        
        best = self.students[0]
        for s in self.students:
            if s.gpa > best.gpa:
                best = s
        
        return best

    def find(self, name):
        found_students = []
        for s in self.students:
            if name in s.name:
                found_students.append(s)
        return found_students