class Pet:
    def __init__(self, name, price, age):
        self.__name = name
        self.__price = price
        self.__age = age

    @property
    def name(self):         # similar to get_name()
        return self.__name
    
    @name.setter
    def name(self, name):  # similar to set_name()
        if name == '':
            print('Name cannot be empty')
        else:
            self.__name = name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price < 0:
            print('Price cannot be negative')
        else:
            self.__price = price
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 0:
            print('Age cannot be negative')
        else:
            self.__age = age


dogo = Pet('Dog', 100, 5)
dogo.name = 'Poodle'
dogo.price = 200
dogo.age = 2

print(f'Name: {dogo.name}, price: {dogo.price}, age: {dogo.age}')