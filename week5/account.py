class Account:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name
        self.__balance = balance

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if id < 0:
            print('ID cannot be negative')
        else:
            self.__id = id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == '':
            print('Name cannot be empty')
        else:
            self.__name = name
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        if balance < 0:
            print('Balance cannot be negative')
        else:
            self.__balance = balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print('Invalid amount. Transaction cancelled.')
        elif amount > self.__balance:
            print('Insufficient balance. Transaction cancelled.')
        else:
            self.__balance -= amount # self.balance -= amount
            print(f'Withdraw successful. New balance: ${self.balance}')

    def deposit(self, amount):
        if amount <= 0:
            print('Invalid amount. Transaction cancelled.')
        else:
            self.balance += amount
            print(f'Deposit successful. New balance: ${self.balance}')
    
    def transfer(self, amount, other):
        if amount <= 0:
            print('Invalid amount. Transaction cancelled.')
        elif amount > self.balance:
            print('Insufficient balance. Transaction cancelled.')
        else:
            self.balance -= amount
            other.balance += amount
            print(f'Transfer successful. New balance: ${self.balance}')
    
    def show(self):
        print(f'Account ID: {self.id}, name: {self.name}, balance: ${self.balance}')