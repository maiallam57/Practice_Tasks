from abc import abstractmethod,ABCMeta
from math import sqrt
from time import sleep

class Polygon(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def Area(self):
        pass
    @abstractmethod
    def Perimeter(self):
        pass
class Circles(Polygon):
    def __init__(self):
        super().__init__()
        self.radius = 0.0
    def Area(self):
        return ((22/7) * self.radius**2)
    def Perimeter(self):
        return (2*(22/7)*self.radius)
    def findCircle(self):
        try:
            radius = float(input("\nTo Calculate The Area And The Perimeter Of The Circle..\nPlease Enter Radius Of The Circle: "))
            sleep(0.3)
            self.radius=radius
            print(f"\nThe Area= {self.Area()} \nThe Perimeter={self.Perimeter()} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findCircle()
class Triangles(Polygon):
    def Area(self):
        pass
    def Perimeter(self):
        pass
class EquilateralTriangle(Triangles):
    def __init__(self):
        super().__init__()
        self.side=0.0
    def Area(self):
        return ((sqrt(3)/4)*(self.side**2))
    def Perimeter(self):
        return (self.side*3)
    def findEquilateralTriangle(self):
        try:
            side = float(input("To Calculate The Area And The Perimeter Of The Equilateral Triangle..\nPlease Enter The Side Of The Equilateral Triangle: "))
            self.side=side
            print(f"\nThe Area= {self.Area()} \n The Perimeter={self.Perimeter()} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findEquilateralTriangle()
class IsoscelesTriangle(Triangles):
    def __init__(self):
        super().__init__()
        self.side1 = 0.0
        self.base=0.0
        self.height=0.0
    def Area(self):
        return (0.5*self.base*self.height)
    def Perimeter(self):
        return ((self.side1*2)+self.base)
    def findIsoscelesTriangle(self):
        try:
            base = float(input("\nTo Calculate The Area And The Perimeter Of The Isosceles Triangle..\nPlease Enter The Base Of The Isosceles Triangle: "))
            sleep(0.3)
            height = float(input("\nPlease Enter The Height Of The Isosceles Triangle: "))
            sleep(0.3)
            side1 = float(input("\nPlease Enter The Side Of The Isosceles Triangle: "))
            sleep(0.3)
            self.base=base
            self.height=height
            self.side1=side1
            print(f"\nThe Area= {self.Area()} \nThe Perimeter={self.Perimeter()} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findIsoscelesTriangle()
class Quadrilaterals(Polygon):
    def __init__(self):
        super().__init__()
    def Area(self):
        pass
    def Perimeter(self):
        pass
class Trapezoid(Quadrilaterals):
    def __init__(self):
        super().__init__()
        self.longBase =0.0
        self.shortBase = 0.0
        self.side1 = 0.0
        self.side2 = 0.0
        self.height = 0.0
    def Area(self):
        return (0.5 * (self.longBase+self.shortBase) * self.height)
    def Perimeter(self):
        return (self.longBase+self.shortBase+self.side1+self.side2)
    def findTrapezoid(self):
        try:
            longBase = float(input("\nTo Calculate The Area And The Perimeter Of The Trapezoid..\nPlease Enter The longBase Of The Trapezoid: "))
            sleep(0.3)
            shortBase = float(input("\nPlease Enter The shortBase Of The Trapezoid: "))
            sleep(0.3)
            side1 = float(input("\nPlease Enter The First Side Of The Trapezoid: "))
            sleep(0.3)
            side2 = float(input("\nPlease Enter The Second Side Of The Trapezoid: "))
            sleep(0.3)
            height = float(input("\nPlease Enter The Height Of The Trapezoid: "))
            sleep(0.3)
            self.longBase=longBase
            self.shortBase = shortBase
            self.side1 = side1
            self.side2 = side2
            self.height = height
            print(f"\nThe Area= {self.Area()} \nThe Perimeter= {self.Perimeter()} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findTrapezoid()
class Parallelogram(Quadrilaterals):
    def __init__(self):
        super().__init__()
        self.base = 0.0
        self.side = 0.0
        self.height = 0.0
    def Area(self):
        return (self.base*self.height)
    def Perimeter(self):
        return (2*(self.base+self.side))
    def findParallelogram(self):
        try:
            base = float(input("\nTo Calculate The Area And The Perimeter Of The Parallelogram..\nPlease Enter The Base Of The Parallelogram: "))
            sleep(0.3)
            side = float(input("\nPlease Enter The Side Of The Parallelogram: "))
            sleep(0.3)
            height = float(input("\nPlease Enter The Height  Of The Parallelogram: "))
            sleep(0.3)
            self.base = base
            self.side = side
            self.height = height
            print(f"\nThe Area= {self.Area()} \nThe Perimeter={self.Perimeter()} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findParallelogram()
class Rhombus(Quadrilaterals):
    def __init__(self):
        super().__init__()
        self.side = 0.0
        self.longdiagonal = 0.0
        self.shortdiagonal = 0.0
    def Area(self):
        return (0.5*self.longdiagonal*self.shortdiagonal)
    def Perimeter(self):
        return (self.side*4)
    def findRhombus(self):
        try:
            side = float(input("\nTo Calculate The Area And The Perimeter Of The Rhombus..\nPlease Enter The Side Of The Rhombus: "))
            sleep(0.3)
            longdiagonal = float(input("\nPlease Enter The Longdiagonal Of The Rhombus: "))
            sleep(0.3)
            shortdiagonal = float(input("\nPlease Enter The Shortdiagonal  Of The Rhombus: "))
            sleep(0.3)
            self.side = side
            self.longdiagonal = longdiagonal
            self.shortdiagonal = shortdiagonal
            print(f"\nThe Area= {self.Area()} \nThe Perimeter={self.Perimeter()} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findRhombus()
class Rectangle(Quadrilaterals):
    def __init__(self):
        super().__init__()
        self.length = 0.0
        self.width=0.0
    def Area(self):
        return (self.length*self.width)
    def Perimeter(self):
        return (2*(self.length+self.width))
    def findRectangle(self):
        try:
            lenght = float(input("\nTo Calculate The Area And The Perimeter Of The Rectangle..\nPlease Enter The Lenght Of The Rectangle: "))
            sleep(0.3)
            width = float(input("\nPlease Enter The Width Of The Rectangle: "))
            sleep(0.3)
            self.length = lenght
            self.width = width
            print(f"\nThe Area= {self.Area()} \nThe Perimeter={self.Perimeter()} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findRectangle()
class Square(Quadrilaterals):
    def __init__(self):
        super().__init__()
        self.side = 0.0
    def Area(self):
        return (self.side**2)
    def Perimeter(self):
        return (self.side * 4)
    def findSquare(self):
        try:
            side = float(input("\nTo Calculate The Area And The Perimeter Of The Square..\nPlease Enter The Side Of The Square: "))
            sleep(0.3)
            self.side = side
            print(f"\nThe Area= {self.Area()} \nThe Perimeter={self.Perimeter()} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findSquare()
class Pentagon(Polygon):
    def __init__(self):
        super().__init__()
        self.sideLength = 0.0
        self.apothem=0.0
    def Area(self):
        return (0.5*self.Perimeter()*self.apothem)
    def Perimeter(self):
        return (self.sideLength *5)
    def findPentagon(self):
        try:
            sideLength = float(input("\nTo Calculate The Area And The Perimeter Of The Pentagon..\nPlease Enter The Side Length Of The Pentagon: "))
            sleep(0.3)
            apothem = float(input("\nPlease Enter The apothem..\n(The Perpendicular Distance Between The Center Of The Pentagon): "))
            sleep(0.3)
            self.sideLength = sideLength
            self.apothem = apothem
            print(f"\nThe Area= {self.Area()} \nThe Perimeter={self.Perimeter()} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findPentagon()
class Hexagon(Polygon):
    def __init__(self):
        super().__init__()
        self.sideLength = 0.0
        self.apothem=0.0
    def Area(self):
        return (0.5*self.Perimeter()*self.apothem)
    def Perimeter(self):
        return (self.sideLength *6)
    def findHexagon(self):
        try:
            sideLength = float(input("\nTo Calculate The Area And The Perimeter Of The Hexagon..\nPlease Enter The Side Length Of The Hexagon: "))
            sleep(0.3)
            apothem = float(input("\nPlease Enter The apothem..\n(The Perpendicular Distance Between The Center Of The Hexagon): "))
            sleep(0.3)
            self.sideLength = sideLength
            self.apothem = apothem
            print(f"\nThe Area= {self.Area()} \nThe Perimeter={self.Perimeter()} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findHexagon()
class Octagon(Polygon):
    def __init__(self):
        super().__init__()
        self.sideLength = 0.0
        self.apothem=0.0
    def Area(self):
        return (0.5*self.Perimeter()*self.apothem)
    def Perimeter(self):
        return (self.sideLength *8)
    def findOctagon(self):
        try:
            sideLength = float(input("\nTo Calculate The Area And The Perimeter Of The Octagon..\nPlease Enter The Side Length Of The Octagon: "))
            sleep(0.3)
            apothem = float(input("\nPlease Enter The apothem..\n(The Perpendicular Distance Between The Center Of The Octagon): "))
            sleep(0.3)
            self.sideLength = sideLength
            self.apothem = apothem
            print(f"\nThe Area= {self.Area()} \nThe Perimeter={self.Perimeter()} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findOctagon()
class ProgramLoop():
    def __init__(self):
        self.loop()
    def welcomeInfo(self):
        print("\nWELCOME TO AREA AND PERIMETER CALCULATOR!\n")
        sleep(1)
        print("To Calculate The Area And The Perimeter,Please Choose A Category..")
        sleep(0.3)
        print("Circles,          Enter Number: 1")
        sleep(0.3)
        print("Triangles,        Enter Number: 2")
        sleep(0.3)
        print("Quadrilaterals,   Enter Number: 3")
        sleep(0.3)
        print("Regular Polygons, Enter Number: 4")
        sleep(0.3)
        print("To Exit,          Enter Number: 5\n")
        sleep(0.3)
    def getInput(self):
        try:
            firstInput = int(input("Please Enter Your Choice: "))
            if firstInput >= 1 and firstInput <= 5:
                return firstInput
            else:
                print('OUT OF RANGE!,Please Try Again..')
                self.getInput()
        except:
            print("INVAILD INPUT!,Please Try Again")
            self.getInput()
    def findPolygon(self, firstInput):
        if firstInput == 1:
            myCircles=Circles()
            myCircles.findCircle()
        elif firstInput == 2:
            print("\nPlease Choose A Triangle Type..")
            sleep(0.3)
            print("EquilateralTriangle, Enter Number: 1")
            sleep(0.3)
            print("IsoscelesTriangle,   Enter Number: 2")
            sleep(0.3)
            try:
                triangleChoice = int(input("\nPlease Enter Your Choice: "))
                sleep(0.3)
                if triangleChoice == 1:
                    myEquilateral=EquilateralTriangle()
                    myEquilateral.findEquilateralTriangle()
                elif triangleChoice == 2:
                    myIsosceles=IsoscelesTriangle()
                    myIsosceles.findIsoscelesTriangle()
                else:
                    print('\nOUT OF RANGE!,Please Try Again..')
                    self.findPolygon(firstInput)
            except:
                print("\nINVAILD INPUT!,Please Try Again")
                self.findPolygon(firstInput)
        elif firstInput == 3:
            print("\nPlease Choose A Quadrilateral Type..")
            sleep(0.3)
            print("Trapezoid,     Enter Number: 1")
            sleep(0.3)
            print("Parallelogram, Enter Number: 2")
            sleep(0.3)
            print("Rhombus,       Enter Number: 3")
            sleep(0.3)
            print("Rectangle,     Enter Number: 4")
            sleep(0.3)
            print("Sqaure,        Enter Number: 5\n")
            sleep(0.3)
            try:
                QuadrilateralChoice = int(input("\nPlease Enter Your Choice: "))
                sleep(0.3)
                if QuadrilateralChoice == 1:
                    myTrapezoid=Trapezoid()
                    myTrapezoid.findTrapezoid()
                elif QuadrilateralChoice == 2:
                    myParallelogram=Parallelogram()
                    myParallelogram.findParallelogram()
                elif QuadrilateralChoice == 3:
                    myRhombus=Rhombus()
                    myRhombus.findRhombus()
                elif QuadrilateralChoice == 4:
                    myRectangle=Rectangle()
                    myRectangle.findRectangle()
                elif QuadrilateralChoice == 5:
                    mySquare=Square()
                    mySquare.findSquare()
                else:
                    print('\nOUT OF RANGE!,Please Try Again..')
                    self.findPolygon(firstInput)
            except:
                print("\nINVAILD INPUT!,Please Try Again")
                self.findPolygon(firstInput)
        elif firstInput == 4:
            print("\nPlease Choose A Regular Polygon Type..")
            sleep(0.3)
            print("Pentagon, Enter Number: 1")
            sleep(0.3)
            print("Hexagon,  Enter Number: 2")
            sleep(0.3)
            print("Octagon,  Enter Number: 3\n")
            sleep(0.3)
            try:
                RegularChoice = int(input("\nPlease Enter Your Choice: "))
                sleep(0.3)
                if RegularChoice == 1:
                    myPentagon=Pentagon()
                    myPentagon.findPentagon()
                elif RegularChoice == 2:
                    myHexagon=Hexagon()
                    myHexagon.findHexagon()
                elif RegularChoice == 3:
                    myOctagon=Octagon()
                    myOctagon.findOctagon()
                else:
                    print('\nOUT OF RANGE!,Please Try Again..')
                    self.findPolygon(firstInput)
            except:
                print("\nINVAILD INPUT!,Please Try Again")
                self.findPolygon(firstInput)
        elif firstInput == 5:
            pass
    def loop(self):
        self.notExit = True
        while self.notExit:
            self.welcomeInfo()
            self.findPolygon(self.getInput())
            try:
                exitChoice = int(input("\nDo You Want To Calculate The Area And The Perimeter Another Time..\nYes! Enter 1\nNo!  Enter 2\nPlease Enter Your Choice: "))
                if exitChoice == 1:
                    continue
                elif exitChoice == 2:
                    print("\nTHE END!")
                    self.notExit = False
                    break
            except:
                print("\nINVAILD INPUT!,Please Try Again")

myProgram=ProgramLoop()