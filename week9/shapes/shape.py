class Shape:
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
    
    def area(self):
        return 0.0
    
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