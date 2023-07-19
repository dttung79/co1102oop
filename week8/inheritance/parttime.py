from employee import Employee

class PartTimeEmployee(Employee):
    def __init__(self, name, rate, days):
        super().__init__(name, rate)
        self.__days = days
    
    @property
    def days(self):
        return self.__days
    
    @days.setter
    def days(self, days):
        if days < 1 or days > 5:
            raise ValueError("Days must be between 1 and 5")
        self.__days = days

    def salary(self):
        return super().salary() * self.days / 5
    
    def show_info(self):
        super().show_info()
        print(f', working days: {self.days}', end='')