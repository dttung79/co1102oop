from account import Account

class Bank:
    def __init__(self, name):
        self.__name = name
        self.__accounts = []
    
    def add_account(self, acc):
        self.__accounts.append(acc)
        print(f'Account {acc.id} added.')
    
    def show_all(self):
        print(f'Bank: {self.__name}')
        print('Accounts:')
        for acc in self.__accounts:
            acc.show()
    
    def __get_account(self, id):
        for acc in self.__accounts:
            if acc.id == id:
                return acc
        return None
    
    def show_account(self, id):
        acc = self.__get_account(id)
        if acc == None:
            print(f'Account {id} not found.')
        else:
            acc.show()

    def withdraw(self, id, amount):
        acc = self.__get_account(id)
        if acc == None:
            print(f'Account {id} not found.')
        else:
            acc.withdraw(amount)
    
    def deposit(self, id, amount):
        acc = self.__get_account(id)
        if acc == None:
            print(f'Account {id} not found.')
        else:
            acc.deposit(amount)
    
    def transfer(self, source_id, destination_id, amount):
        source_acc = self.__get_account(source_id)
        dest_acc = self.__get_account(destination_id)
        if source_acc == None:
            print(f'Account {source_id} not found.')
        elif dest_acc == None:
            print(f'Account {destination_id} not found.')
        else:
            source_acc.transfer(amount, dest_acc)
#### Test Bank & Account
bank = Bank('Tienphong Bank')
acc1 = Account(1, 'John', 1000)
acc2 = Account(2, 'Mary', 2000)
acc3 = Account(3, 'Peter', 3000)

bank.add_account(acc1)
bank.add_account(acc2)
bank.add_account(acc3)

bank.show_all()

bank.withdraw(1, 500)       # withdraw $500 from account id 1
bank.deposit(2, 1000)       # deposit $1000 to account id 2
bank.transfer(2, 3, 500)    # transfer $500 from account id 2 to account id 3