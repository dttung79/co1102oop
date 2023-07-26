from abc import ABC, abstractmethod
# declare an abstract class Shape
class Shape(ABC):
    def __init__(self, name):
        self.__check_name(name)
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self.__check_name(value)
        self._name = value
    
    def __check_name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
    
    @abstractmethod
    def area(self):
        pass
    
    def __str__(self):
        return f'Name: {self._name}, area: {self.area()}'
    
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.__check_radius(radius)
        self.__radius = radius
    
    def __check_radius(self, radius):
        if radius <= 0:
            raise ValueError('Radius must be positive')
        
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        self.__check_radius(value)
        self.__radius = value

    def area(self):
        return 3.14 * self.__radius ** 2
    
    def __str__(self):
        super_info = super().__str__()
        return f'{super_info}, radius: {self.__radius}'

class Rectangle(Shape):
    def __init__(self, name, width, height):
        self._check_side(width)
        self._check_side(height)

        super().__init__(name)
        self._width = width
        self._height = height

    def _check_side(self, value):
        if value <= 0:
            raise ValueError('Side must be positive')
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._check_side(value)
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._check_side(value)
        self._height = value
    
    def area(self):
        return self._width * self._height
    
    def __str__(self):
        super_info = super().__str__()
        return f'{super_info}, width: {self._width}, height: {self._height}'
    
class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)

    @property
    def side(self):
        return self.width
    
    @side.setter
    def side(self, value):
        self.width = value
        self.height = value


class Triange(Shape):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.__check_sides(a, b, c)
        self._sidea = a
        self._sideb = b
        self._sidec = c
    
    def __check_sides(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Side must be positive')
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('Invalid sides')
    
    @property
    def sidea(self):
        return self._sidea
    
    @sidea.setter
    def sidea(self, value):
        self.__check_sides(value, self._sideb, self._sidec)
        self._sidea = value

    @property
    def sideb(self):
        return self._sideb
    
    @sideb.setter
    def sideb(self, value):
        self.__check_sides(self._sidea, value, self._sidec)
        self._sideb = value

    @property
    def sidec(self):
        return self._sidec
    
    @sidec.setter
    def sidec(self, value):
        self.__check_sides(self._sidea, self._sideb, value)
        self._sidec = value
    
    def area(self):
        p = (self._sidea + self._sideb + self._sidec) / 2
        return (p * (p - self._sidea) * (p - self._sideb) * (p - self._sidec)) ** 0.5
    
    def __str__(self):
        super_info = super().__str__()
        return f'{super_info}, sidea: {self._sidea}, sideb: {self._sideb}, sidec: {self._sidec}'
    

t = Triange('Triangle 1', 3, 4, 5)
print(t)