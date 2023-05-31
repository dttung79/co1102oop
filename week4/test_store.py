from product import Product
from store import Store

p1 = Product('Phone', 340, 10)
p2 = Product('PC', 1420, 20)
p3 = Product('Monitor', 24, 0)
p4 = Product('Mouse', 12, 50)
p5 = Product('Keyboard', 23, 0)

s = Store()
s.add(p1)
s.add(p2)
s.add(p3)
s.add(p4)
s.add(p5)

print('All products in store:')
s.show_all()

empty_stock = s.find_empty()
print('Empty stock:')
for p in empty_stock:
    p.show_info()
    print('------------------')

name = input('Enter product name to search: ')
p = s.find(name)
if p is not None:
    p.show_info()
else:
    print(f'Product with {name} not found')