class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    def show_info(self):
        print(f'Employee name: {self.__name}, salary: ${self.__salary}')
    
    # provide read access for attribute name
    def get_name(self):
        return self.__name
    
    # provide write access for attribute name
    def set_name(self, name):
        if name == '':
            print('Name cannot be empty')
        else:
            self.__name = name

    # provide read / write accesses for attribute salary
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary < 0:
            print('Salary cannot be negative')
        else:
            self.__salary = salary

john = Employee('John', 1000)
john.show_info()

john.set_name('John Smith')
john.show_info()

john.set_salary(-1200)
john.set_name('')
john.show_info()

print(john.get_name())
print(john.__name)

