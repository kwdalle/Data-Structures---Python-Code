# polygon.py
# Kevin Dalle
# kdalle1@stu.parkland.edu
# CSC 220, Spring 2015

if __name__ == '__main__':
    import polygon
    import sys

    ifilename = sys.argv[1]
    ofilename = sys.argv[2]

    inputfile = open(ifilename, "r")
    outputfile = open(ofilename, "w")
    
    for line in inputfile:
        temp = line.split(",")
        try:
            if temp[0] == "Triangle" or temp[0] == "triangle":
                temp2 = polygon.Triangle(float(temp[1]), float(temp[2]),
                                         float(temp[3]))
                temp2.calc_area()
                temp2.calc_perimeter()
                print(
                    'Triangle,' + '{number:.{digits}f}'.format(number=
                                                              temp2.get_area(),
                                                              digits=2), ',',
                    '{number:.{digits}f}'.format(number=temp2.get_perimeter(),
                                                 digits=2), file=outputfile)
            elif temp[0] == "Isosceles Triangle" or temp[0] == "isosceles triangle":
                temp2 = polygon.IsoscelesTriangle(float(temp[1]), float(temp[2]))
                temp2.calc_area()
                temp2.calc_perimeter()
                print(
                    'Isosceles Triangle,'+
                    '{number:.{digits}f}'.format(number=temp2.get_area(),
                                                 digits=2)+ ','+
                    '{number:.{digits}f}'.format(number=temp2.get_perimeter(),
                                                 digits=2), file=outputfile)
            elif temp[0] == "Equilateral Triangle" or temp[0] == "equilateral triangle":
                temp2 = polygon.EquilateralTriangle(float(temp[1]))
                temp2.calc_area()
                temp2.calc_perimeter()
                print(
                    'Equilateral Triangle,'+
                    '{number:.{digits}f}'.format(number=temp2.get_area(),
                                                 digits=2)+ ','+
                    '{number:.{digits}f}'.format(number=temp2.get_perimeter(),
                                                 digits=2), file=outputfile)
            elif temp[0] == "Quadrilateral" or temp[0] == "quadrilateral":
                temp2 = polygon.Quadrilateral(float(temp[1]), float(temp[2]),
                                              float(temp[3]), float(temp[4]))
                temp2.calc_perimeter()
                temp2.calc_area()
                print(
                    'Quadrilateral,'+
                    '{number:.{digits}f}'.format(number=temp2.get_area(),
                                                 digits=2)+ ','+
                    '{number:.{digits}f}'.format(number=temp2.get_perimeter(),
                                                 digits=2), file=outputfile)
            elif temp[0] == "Rectangle" or temp[0] == "rectangle":
                temp2 = polygon.Rectangle(float(temp[1]), float(temp[2]))
                temp2.calc_area()
                temp2.calc_perimeter()
                print(
                    'Rectangle,'+
                    '{number:.{digits}f}'.format(number=temp2.get_area(),
                                                 digits=2)+ ','+
                    '{number:.{digits}f}'.format(number=temp2.get_perimeter(),
                                                 digits=2), file=outputfile)
            elif temp[0] == "Square" or temp[0] == "square":
                temp2 = polygon.Square(float(temp[1]))
                temp2.calc_area()
                temp2.calc_perimeter()
                print(
                    'Square,',
                    '{number:.{digits}f}'.format(number=temp2.get_area(),
                                                 digits=2)+ ','+
                    '{number:.{digits}f}'.format(number=temp2.get_perimeter(),
                                                 digits=2), file=outputfile)
            elif temp[0] == "Pentagon" or temp[0] == "pentagon":
                temp2 = polygon.Pentagon(float(temp[1]))
                temp2.calc_area()
                temp2.calc_perimeter()
                print(
                    'Pentagon,'+
                    '{number:.{digits}f}'.format(number=temp2.get_area(),
                                                 digits=2)+ ','+
                    '{number:.{digits}f}'.format(number=temp2.get_perimeter(),
                                                 digits=2), file=outputfile)
            elif temp[0] == "Hexagon" or temp[0] == "hexagon":
                temp2 = polygon.Hexagon(float(temp[1]))
                temp2.calc_area()
                temp2.calc_perimeter()
                print(
                    'Hexagon,'+
                    '{number:.{digits}f}'.format(number=temp2.get_area(),
                                                 digits=2)+ ','+
                    '{number:.{digits}f}'.format(number=temp2.get_perimeter(),
                                                 digits=2), file=outputfile)
            elif temp[0] == "Octagon" or temp[0] == "octagon":
                temp2 = polygon.Octagon(float(temp[1]))
                temp2.calc_area()
                temp2.calc_perimeter()
                print(
                    'Octagon,'+
                    '{number:.{digits}f}'.format(number=temp2.get_area(),
                                                 digits=2)+ ','+
                    '{number:.{digits}f}'.format(number=temp2.get_perimeter(),
                                                 digits=2), file=outputfile)
        except ValueError:
            print('You have listed or entered a length that is less than 0,'
                  'please enter a valid entry')

    inputfile.close()
    outputfile.close()
