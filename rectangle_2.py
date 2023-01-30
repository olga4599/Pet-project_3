from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

sq_1 = Square(3)
sq_2 = Square(12)

circle_1 = Circle(7)
circle_2 = Circle(10)

figures = [rect_1, rect_2, sq_1, sq_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print("Squre area:", figure.get_area_sq())
    elif isinstance(figure, Rectangle):
        print("Rectangle area", figure.get_area())
    else:
        print("Circle area: ", figure.get_area_circle())