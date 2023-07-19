class Parent:
    def __init__(self, money):
        self._money = money

class Child(Parent):
    def show(self):
        print(self._money)



c = Child(100)
c.show()

print(c._money)