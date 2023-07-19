from employee import Employee
from parttime import PartTimeEmployee

class Company:
    def __init__(self, name):
        self.__name = name
        self.__full_times = []
        self.__part_times = []

    def add_full(self, emp):
        self.__full_times.append(emp)

    def add_part(self, emp):
        self.__part_times.append(emp)
    
    def show_employees(self):
        print('Full time employees:')
        for e in self.__full_times:
            e.show_info()
            print()
        
        print('\nPart time employees:')
        for e in self.__part_times:
            e.show_info()
            print()