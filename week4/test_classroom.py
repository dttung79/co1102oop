from classroom import ClassRoom
from student import Student

# Create a classroom object
c = ClassRoom()

# Create some student objects
s1 = Student("Hoang", 1, 3.5)
s2 = Student("Huy", 2, 3.0)
s3 = Student("Hieu", 3, 5.0)
s4 = Student("Hoa", 4, 2.5)

# Add students to the classroom
c.add(s1)
c.add(s2)
c.add(s3)
c.add(s4)

best = c.find_best()
print(f'Best student is {best.name} with GPA {best.gpa}')

founds = c.find('o')
for s in founds:
    s.show_info()

id = int(input('Enter student id to revmove: '))
c.remove(id)