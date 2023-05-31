class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def show_info(self):
        print(f'Name: {self.name}')
        print(f'Price: {self.price}')
        print(f'Stock: {self.stock}')

    def get_value(self):
        return self.price * self.stock