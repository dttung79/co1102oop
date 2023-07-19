from menu import MenuProgram
from account import Account, NormalAccount, VIPAccount, DebitAccount

class BankProgram(MenuProgram):
    def __init__(self):
        self.__normal_accounts = []
        self.__vip_accounts = []
        self.__debit_accounts = []
    
    def _print_menu(self):
        print('1. Add normal account')
        print('2. Add VIP account')
        print('3. Add debit account')
        print('4. Search account')
        print('5. Deposit')
        print('6. Withdraw')
    
    def _do_task(self, choice):
        if choice == 1:
            self.__add_normal()
        elif choice == 2:
            self.__add_vip()
        elif choice == 3:
            self.__add_debit()
        elif choice == 4:
            self.__search()
        elif choice == 5:
            self.__deposit()
        elif choice == 6:
            self.__withdraw()
        elif choice == 0:
            print('Goodbye')
        else:
            print('Invalid choice')
    
    def __add_normal(self):
        name = input('Enter name: ')
        id = input('Enter id: ')
        fee = int(input('Enter fee: '))
    
        account = NormalAccount(name, id, fee)
        self.__normal_accounts.append(account)
    
    def __add_debit(self):
        name = input('Enter name: ')
        id = input('Enter id: ')
        limit = int(input('Enter limit: '))
    
        account = DebitAccount(name, id, limit)
        self.__debit_accounts.append(account)
    
    def __add_vip(self):
        name = input('Enter name: ')
        id = input('Enter id: ')
    
        account = VIPAccount(name, id)
        self.__vip_accounts.append(account)
    
    def __search(self):
        id = input('Enter id to search: ')
    
        account = self.__find_account(id)
        if account is None:
            print('Account not found')
        else:
            print(f'Account found: {account.name}, {account.balance}')
    
    def __find_account(self, id):
        for account in self.__normal_accounts:
            if account.id == id:
                return account
        
        for account in self.__vip_accounts:
            if account.id == id:
                return account
        
        for account in self.__debit_accounts:
            if account.id == id:
                return account
            
    def __deposit(self):
        id = input('Enter id to deposit: ')
        amount = int(input('Enter amount to deposit: '))
    
        account = self.__find_account(id)
        if account is None:
            print('Account not found')
        else:
            account.deposit(amount)
            print(f'Update account: {account.name}, {account.balance}')
    
    def __withdraw(self):
        id = input('Enter id to withdraw: ')
        amount = int(input('Enter amount to withdraw: '))
    
        account = self.__find_account(id)
        if account is None:
            print('Account not found')
        else:
            account.withdraw(amount)
            print(f'Update account: {account.name}, {account.balance}')


if __name__ == '__main__':
    program = BankProgram()
    program.run()