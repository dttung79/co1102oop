from product import Product
from store import Store


class StoreProgram:
    def __init__(self, s):
        self.store = s
    
    def print_menu(self):
        print('1. Add product')
        print('2. Remove product')
        print('3. Show all products')
        print('4. Find product')
        print('5. Find empty products')
    
    def get_option(self):
        while True:
            option = int(input('Enter option: '))
            if option >= 1 and option <= 5:
                return option
            print('Invalid option. Try again')
    
    def do_task(self, option):
        if option == 1:
            name = input('Enter new product name: ')
            price = float(input('Enter new product price: '))
            stock = int(input('Enter new product stock: '))
            p = Product(name, price, stock)
            self.store.add(p)
        elif option == 2:
            name = input('Enter name to remove: ')
            self.store.remove(name) 
        elif option == 3:
            self.store.show_all()
        elif option == 4:
            name = input('Enter product name to search: ')
            p = self.store.find(name)
            if p is not None:
                p.show_info()
            else:
                print(f'Product with {name} not found')
        elif option == 5:
            empty_stock = self.store.find_empty()
            if len(empty_stock) == 0:
                print('No empty stock')
            else:
                print('Empty stock products:')
                for p in empty_stock:
                    p.show_info()
                    print('------------------')
    
    def run(self):
        while True:
            self.print_menu()
            option = self.get_option()
            self.do_task(option)
            print('------------------')



#### MAIN PROGRAM ####
s = Store()
program = StoreProgram(s)
program.run()