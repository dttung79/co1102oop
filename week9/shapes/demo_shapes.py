from shape import Shape, Circle, Rectangle

shapes = []

circle = Circle('Circle 1', 5)
shapes.append(circle)

rectangle = Rectangle('Rectangle 1', 10, 20)
shapes.append(rectangle)

for s in shapes:
    print(s)