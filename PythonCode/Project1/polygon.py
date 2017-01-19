# polygon.py
# Kevin Dalle
# kdalle1@stu.parkland.edu
# CSC 220, Spring 2015


class Polygon:
    """Base class for all polygons, from which they are derived from, provides a
    starting point for area and perimeter and provides getters and setters for
    both"""

    def __init__(self):
        self.__area = 0
        self.__perimeter = 0

    def get_area(self):
        return self.__area

    def set_area(self, narea):
        self.__area = narea

    def get_perimeter(self):
        return self.__perimeter

    def set_perimeter(self, nperimeter):
        self.__perimeter = nperimeter

    def calc_perimeter(self):
        # Purely used to force the other classes to use this name
        print('intentionally left empty')

    def calc_area(self):
        # Purely used to force the other classes to use this name
        print('Intentionally left empty')

    def reg_polygon(self, sides, length):
        # This function was defined in the base class because three separate
        # classes use it, this way they all inherit it
        import math

        perim = length * sides

        apothem = length/(2*math.tan(math.pi/sides))

        return (apothem * perim) / 2


class Triangle(Polygon):
    """This class is an extention of the base class and will handle all
    triangles that are neither isoceles or equilateral can produce there area
    and perimeter"""


    def __init__(self, side1, side2, side3):
        super().__init__()
        # Makes sure that every side is at least greater than 0, if not it
        # raises an error
        
        if side1 > 0 and side2 > 0 and side3 > 0:
            self.__side1 = side1
            self.__side2 = side2
            self.__side3 = side3
        else: 
            raise ValueError

    def calc_area(self):
        # Calculates the area based on a formula for the triangle that does not
        # use trigonometry
        import math
        self.calc_perimeter()
        semi = self.get_perimeter()/2
        self.set_area(math.sqrt((semi*(semi-self.__side1)*(semi-self.__side2) *
                                 (semi-self.__side3))))

    def calc_perimeter(self):
        # Simply adds all the sides up to get the perimeter
        self.set_perimeter(self.__side1 + self.__side2 + self.__side3)
      


class IsoscelesTriangle(Triangle):
    """This class is an extention of the Triangle class, and therefore the
    Polygon class, this class will deal with Isosceles triangles only can
    produce there area and perimeter"""

    def __init__(self, base, height):
        import math
        if base > 0 and height > 0:
            # Insures that the height and is at least greater than 0 and if so
            # calculates the sides
            self.__base = base
            self.__height = height
            self.__side = math.sqrt(((1/2)*self.__base)**2 + self.__height**2)
        else:
            raise ValueError

        # The __init__ function of the inherited classes are called, and that
        # means that it will check the sides to make sure they are valid and
        # passes the sides for the perimeter function.
        super().__init__(self.__base, self.__side, self.__side)

    def calc_area(self):
        # Calculates area based on the basic triangle formula
        self.set_area((1/2)*self.__base*self.__height)

class EquilateralTriangle(Triangle):
    """This class is an extention of the Triangle class, and therefore the
    Polygon class, this class will deal with Equilateral triangles only can
    produce there area and perimeter"""

    def __init__(self, side):
        # Uses the inherited classes inherited __init__ to check for valid input
        # and passes the sides on for the perimeter functions
        super().__init__(side, side, side)

        self.__side = side

    def calc_area(self):
        # Calculates area using a formula for Equilateral Triangles
        import math
        self.set_area((math.sqrt(3)/4)*(self.__side**2))


class Quadrilateral(Polygon):
    """This class is an extention of the polygon class that deals with polygons
    that only have 4 sides can produce there area and perimeter"""

    def __init__(self, side1, side2, side3, side4):
        super().__init__()

        if side1 > 0 and side2 > 0 and side3 > 0 and side4 > 0:
            # Checks to make sure that all input is valid, if not it raises an
            # error.
            self.__side1 = side1
            self.__side2 = side2
            self.__side3 = side3
            self.__side4 = side4
        else:
            raise ValueError

    def calc_perimeter(self):
        # Gets perimeter by adding all the sides together
        self.set_perimeter(self.__side1 + self.__side2 + self.__side3 +
                           self.__side4)

    def calc_area(self):
        # Uses Brahmagupta's formula to calculate the area of the Quadrilateral
        import math
        semi = self.get_perimeter()
        semi /= 2
        self.set_area(math.sqrt((float(semi) - self.__side1) *
                                (float(semi) - self.__side2) *
                                (float(semi) - self.__side3) *
                                (float(semi) - self.__side4)))

class Rectangle(Quadrilateral):
    """This is a extention of the Quad class and therefore the Polygon class,
    and deals with Quads whose coresponding sides are equal can produce there
    area and perimeter"""

    def __init__(self, side1, side2):
        # Checks the input to make sure its valid and passes on the sides for
        # perimeter function
        super().__init__(side1, side2, side1, side2)

        self.__length = side1
        self.__width = side2

    def calc_area(self):
        # Uses the basic formula for Rectangle area
        self.set_area(self.__length*self.__width)


class Square(Rectangle):
    """This is an extention of the Rectangle class therefore the Quad class and
    the Polygon class, and deals with Quads that have all equal sides can
    produce there area and perimeter"""
    def __init__(self, side):
        super().__init__(side, side)
        # Checks the input to make sure its valid and passes on the sides for
        # perimeter function
        
        self.__sides = side
        
    def calc_area(self):
        # Basic square area formula
        self.set_area(self.__sides**2)


class Pentagon(Polygon):
    """This is an extention of the Polygon class that deals with Pentagons and
    will be able to return their area and perimeter"""
    def __init__(self, length):
        super().__init__()
        if length > 0:
            # Checks for valid input
            self.__lengths = length
        else:
            raise ValueError

    def calc_perimeter(self):
        self.set_perimeter(self.__lengths * 5)
        
    def calc_area(self):
        self.set_area(self.reg_polygon(5, self.__lengths))


class Hexagon(Polygon):
    """This is an extentino of the Polygon class that deals only with Hexagons
        and will return their perim and area"""
    
    def __init__(self, length):
        super().__init__()
        if length > 0:
            # Checks for valid input
            self.__lengths = length
        else:
            raise ValueError
    
    def calc_perimeter(self):
        self.set_perimeter(self.__lengths * 6)
        
    def calc_area(self):
        self.set_area(self.reg_polygon(6, self.__lengths))
        
class Octagon(Polygon):
    """This is an extention of the Polygon class that deals only with Octagons
    this function will return the area and perimeter of the shape"""

    def __init__(self, length):
        super().__init__()
        if length > 0:
            # Checks for valid input
            self.__lengths = length
        else:
            raise ValueError

    def calc_perimeter(self):
        self.set_perimeter(self.__lengths * 8)

    def calc_area(self):
        self.set_area(self.reg_polygon(8, self.__lengths))

if __name__ == '__main__':
    first = Triangle(3, 4, 5)
    first.calc_perimeter()
    first.calc_area()
    print('Area Scalene: ', first.get_area())
    print('Perimeter Scalene: ', first.get_perimeter())

    second = IsoscelesTriangle(5, 6)
    second.calc_area()
    second.calc_perimeter()
    print('Area Isosceles: ', second.get_area())
    print('Perimeter Isosceles: ', second.get_perimeter())

    third = EquilateralTriangle(3)
    third.calc_area()
    third.calc_perimeter()
    print('Area Equilateral: ', third.get_area())
    print('Perimeter Equilateral: ', third.get_perimeter())

    fourth = Quadrilateral(1, 2, 3, 4)
    fourth.calc_area()
    fourth.calc_perimeter()
    print('Area Quadrilateral: ', fourth.get_area())
    print('Perimeter Quadrilateral: ', fourth.get_perimeter())

    fifth = Rectangle(1, 2)
    fifth.calc_area()
    fifth.calc_perimeter()
    print('Area Rectangle: ', fifth.get_area())
    print('Perimeter Rectangle: ', fifth.get_perimeter())

    sixth = Square(3)
    sixth.calc_area()
    sixth.calc_perimeter()
    print('Area Square: ', sixth.get_area())
    print('Perimeter Square: ', sixth.get_perimeter())

    seventh = Pentagon(3)
    seventh.calc_area()
    seventh.calc_perimeter()
    print('Area Pentagon: ', seventh.get_area())
    print('Perimeter Pentagon: ', seventh.get_perimeter())

    eighth = Hexagon(4)
    eighth.calc_area()
    eighth.calc_perimeter()
    print('Area Hexagon: ', eighth.get_area())
    print('Perimeter Hexagon: ', eighth.get_perimeter())

    ninth = Octagon(5)
    ninth.calc_area()
    ninth.calc_perimeter()
    print('Area Octagon: ', ninth.get_area())
    print('Perimeter Octagon: ', ninth.get_perimeter())