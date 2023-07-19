class Employee:
    def __init__(self, name, rate):
        self._name = name
        self._rate = rate
        self._BASIC_SALARY = 1000
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def rate(self):
        return self._rate
    
    @rate.setter
    def rate(self, rate):
        self._rate = rate
    
    def salary(self):
        return self._rate * self._BASIC_SALARY
    
    def show_info(self):
        print(f'Name: {self._name}, salary: {self.salary()}', end='')