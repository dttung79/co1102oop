class Account:
    def __init__(self, name, id):
        self._name = name           # read / write access
        self._id = id               # read only access
        self._balance = 0           # read / (indirect) write access
        self._MAC_AMOUNT = 500      # hidden from outsite but the subclass can access it
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        self._name = name
    
    @property
    def id(self):
        return self._id
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Amount must be less than or equal to balance")
        if amount > self._MAC_AMOUNT:
            raise ValueError("Amount must be less than or equal to MAC_AMOUNT")
        self._balance -= amount

class NormalAccount(Account):
    def __init__(self, name, id, fee):
        super().__init__(name, id)
        self.__fee = fee
    
    def withdraw(self, amount):
        if amount > self._balance + self.__fee:
            raise ValueError("Not enough balance")
        
        super().withdraw(amount)
        self._balance -= self.__fee

class VIPAccount(Account):
    def __init__(self, name, id):
        super().__init__(name, id)
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Not enough balance")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        self._balance -= amount

class DebitAccount(Account):
    def __init__(self, name, id, limit):
        super().__init__(name, id)
        self.__litmit = limit
    
    @property
    def limit(self):
        return self.__litmit
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        if amount > self._MAC_AMOUNT:
            raise ValueError(f"Amount must be less than or equal to f{self._MAC_AMOUNT}")
        if amount > self._balance + self.__litmit + 0.05 * amount:
            raise ValueError("Not enough balance")
        if amount > self._balance:
            self._balance = self._balance - amount - 0.05 * amount
        else:
            self._balance -= amount