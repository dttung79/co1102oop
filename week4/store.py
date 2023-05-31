class Store:
    def __init__(self):
        self.products = []
    
    def add(self, p):
        self.products.append(p)
    
    def remove(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                print(f'Product {name} removed')
                return
        print(f'Product with {name} not found')
    
    def show_all(self):
        if len(self.products) == 0:
            print('No products in store')
            return
        
        print('All products in store:')
        for p in self.products:
            p.show_info()
            print(f'Value: {p.get_value()}')
            print('------------------')

    def find(self, name):
        for p in self.products:
            if p.name == name:
                return p
        return None

    def find_empty(self):
        empty_products = []
        for p in self.products:
            if p.stock == 0:
                empty_products.append(p)
        return empty_products