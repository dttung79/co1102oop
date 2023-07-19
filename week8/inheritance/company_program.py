from menu import MenuProgram
from employee import Employee
from parttime import PartTimeEmployee
from company import Company

class CompanyProgram(MenuProgram):
    def __init__(self, name):
        self.__company = Company(name)
    
    def _print_menu(self):
        print('1. Add full-time')
        print('2. Add part-time')
        print('3. Show employees')
        print('0. Exit')

    def _do_task(self, choice):
        if choice == 1:
            self.__add_full()
        elif choice == 2:
            self.__add_part()
        elif choice == 3:
            self.__company.show_employees()
        else:
            print('Invalid choice')
    
    def __add_full(self):
        name = input('Enter employee name: ')
        rate = float(input('Enter employee rate: '))
        emp = Employee(name, rate)
        self.__company.add_full(emp)
    
    def __add_part(self):
        name = input('Enter employee name: ')
        rate = float(input('Enter employee rate: '))
        days = int(input('Enter employee working days: '))
        emp = PartTimeEmployee(name, rate, days)
        self.__company.add_part(emp)
    

program = CompanyProgram('ABC')
program.run()
