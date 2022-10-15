from abc import abstractmethod,ABCMeta
from math import sqrt
from time import sleep

class Polygon(metaclass=ABCMeta):
    def __init__(self,numberOfSides=0):
        self.numberOfSides=numberOfSides
        self.perimeterValue=0.0
        self.areaValue=0.0

    @abstractmethod
    def Area(self):
        pass
    @abstractmethod
    def Perimeter(self):
        pass
class Circles(Polygon):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
        self.areaValue=self.Area()
        self.perimeterValue=self.Perimeter()
    def Area(self):
        return ((22/7) * self.radius**2)
    def Perimeter(self):
        return (2*(22/7)*self.radius)
class Triangles(Polygon):
    def __init__(self):
        super().__init__()
    def Area(self):
        pass
    def Perimeter(self):
        pass
class EquilateralTriangle(Triangles):
    def __init__(self,side):
        super().__init__()
        self.side = side
        self.areaValue = self.Area()
        self.perimeterValue = self.Perimeter()
    def Area(self):
        return ((sqrt(3)/4)*(self.side**2))
    def Perimeter(self):
        return (self.side*3)
class IsoscelesTriangle(Triangles):
    def __init__(self,side1,side2,base,height):
        super().__init__()
        self.side1 = side1
        self.side2=side2
        self.base=base
        self.height=height
        self.areaValue = self.Area()
        self.perimeterValue = self.Perimeter()
    def Area(self):
        return (0.5*self.base*self.height)
    def Perimeter(self):
        return (self.side1+self.side2+self.base)
class Quadrilaterals(Polygon):
    def __init__(self):
        super().__init__()
    def Area(self):
        pass
    def Perimeter(self):
        pass
class Trapezoid(Quadrilaterals):
    def __init__(self,longBase,shortBase,side1,side2,height):
        super().__init__()
        self.longBase = longBase
        self.shortBase = shortBase
        self.side1 = side1
        self.side2 = side2
        self.height = height
        self.areaValue = self.Area()
        self.perimeterValue = self.Perimeter()
    def Area(self):
        return (0.5 * (self.longBase+self.shortBase) * self.height)
    def Perimeter(self):
        return (self.longBase+self.shortBase+self.side1+self.side2)
class Parallelogram(Quadrilaterals):
    def __init__(self,base,side,height):
        super().__init__()
        self.base = base
        self.side = side
        self.height = height
        self.areaValue = self.Area()
        self.perimeterValue = self.Perimeter()
    def Area(self):
        return (self.base*self.height)
    def Perimeter(self):
        return (2*(self.base+self.side))
class Rhombus(Quadrilaterals):
    def __init__(self,side,longdiagonal,shortdiagonal):
        super().__init__()
        self.side = side
        self.longdiagonal = longdiagonal
        self.shortdiagonal = shortdiagonal
        self.areaValue = self.Area()
        self.perimeterValue = self.Perimeter()
    def Area(self):
        return (0.5*self.longdiagonal*self.shortdiagonal)
    def Perimeter(self):
        return (self.side*4)
class Rectangle(Quadrilaterals):
    def __init__(self, lenght,width):
        super().__init__()
        self.length = lenght
        self.width=width
        self.areaValue = self.Area()
        self.perimeterValue = self.Perimeter()
    def Area(self):
        return (self.length*self.width)
    def Perimeter(self):
        return (2*(self.length+self.width))
class Square(Quadrilaterals):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.areaValue = self.Area()
        self.perimeterValue = self.Perimeter()
    def Area(self):
        return (self.side**2)
    def Perimeter(self):
        return (self.side * 4)
class Pentagon(Polygon):
    def __init__(self, sideLength,apothem):
        super().__init__()
        self.sideLength = sideLength
        self.apothem=apothem
        self.areaValue = self.Area()
        self.perimeterValue = self.Perimeter()
    def Area(self):
        return (0.5*self.Perimeter()*self.apothem)
    def Perimeter(self):
        return (self.sideLength *5)
class Hexagon(Polygon):
    def __init__(self, sideLength,apothem):
        super().__init__()
        self.sideLength = sideLength
        self.apothem=apothem
        self.areaValue = self.Area()
        self.perimeterValue = self.Perimeter()
    def Area(self):
        return (0.5*self.Perimeter()*self.apothem)
    def Perimeter(self):
        return (self.sideLength *6)
class Octagon(Polygon):
    def __init__(self, sideLength,apothem):
        super().__init__()
        self.sideLength = sideLength
        self.apothem=apothem
        self.areaValue = self.Area()
        self.perimeterValue = self.Perimeter()
    def Area(self):
        return (0.5*self.Perimeter()*self.apothem)
    def Perimeter(self):
        return (self.sideLength *8)
class FindTheShape():
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
            choice=int(input("Please Enter Your Choice: "))
            if choice>=1 and choice<=5:
                return choice
            else:
                print('OUT OF RANGE!,Please Try Again..')
                self.getInput()
        except:
            print("INVAILD INPUT!,Please Try Again")
            self.getInput()
    def findPolygon(self,firstInput):
        if firstInput==1:
            self.findCircle()
        elif firstInput==2:
            print("\nPlease Choose A Triangle Type..")
            sleep(0.3)
            print("EquilateralTriangle, Enter Number: 1")
            sleep(0.3)
            print("IsoscelesTriangle,   Enter Number: 2")
            sleep(0.3)
            try:
                triangleChoice = int(input("\nPlease Enter Your Choice: "))
                sleep(0.3)
                if triangleChoice==1:
                    self.findEquilateralTriangle()
                elif triangleChoice==2:
                    self.findIsoscelesTriangle()
                else:
                    print('\nOUT OF RANGE!,Please Try Again..')
                    self.findPolygon(firstInput)
            except:
                print("\nINVAILD INPUT!,Please Try Again")
                self.findPolygon(firstInput)
        elif firstInput== 3:
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
                    self.findTrapezoid()
                elif QuadrilateralChoice == 2:
                    self.findParallelogram()
                elif QuadrilateralChoice == 3:
                    self.findRhombus()
                elif QuadrilateralChoice == 4:
                    self.findRectangle()
                elif QuadrilateralChoice == 5:
                    self.findSquare()
                else:
                    print('\nOUT OF RANGE!,Please Try Again..')
                    self.findPolygon(firstInput)
            except:
                print("\nINVAILD INPUT!,Please Try Again")
                self.findPolygon(firstInput)
        elif firstInput==4:
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
                    self.findPentagon()
                elif RegularChoice == 2:
                    self.findHexagon()
                elif RegularChoice == 3:
                    self.findOctagon()
                else:
                    print('\nOUT OF RANGE!,Please Try Again..')
                    self.findPolygon(firstInput)
            except:
                print("\nINVAILD INPUT!,Please Try Again")
                self.findPolygon(firstInput)
        elif firstInput==5:
            pass
    def findCircle(self):
        try:
            radius = float(input("\nTo Calculate The Area And The Perimeter Of The Circle..\nPlease Enter Radius: "))
            sleep(0.3)
            myCircle = Circles(radius)
            print(f"\nThe Area= {myCircle.areaValue} \nThe Perimeter={myCircle.perimeterValue} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findCircle()
    def findEquilateralTriangle(self):
        try:
            side = float(input("To Calculate The Area And The Perimeter Of The Equilateral Triangle..\nPlease Enter The Side Of The Triangle: "))
            myEquilateral = EquilateralTriangle(side)
            print(
                f"\nThe Area= {myEquilateral.areaValue} \n The Perimeter={myEquilateral.perimeterValue} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findEquilateralTriangle()
    def findIsoscelesTriangle(self):
        try:
            base = float(input("\nTo Calculate The Area And The Perimeter Of The Isosceles Triangle..\nPlease Enter The Base Of The Triangle: "))
            sleep(0.3)
            height = float(input("\nPlease Enter The Height Of The Triangle: "))
            sleep(0.3)
            side1 = float(input("\nPlease Enter The First Side Of The Triangle: "))
            sleep(0.3)
            side2 = float(input("\nPlease Enter The Second Side Of The Triangle: "))
            sleep(0.3)
            myIsosceles = IsoscelesTriangle(side1,side2,base,height)
            print(f"\nThe Area= {myIsosceles.areaValue} \nThe Perimeter={myIsosceles.perimeterValue} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findIsoscelesTriangle()
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
            myTrapezoid = Trapezoid(longBase,shortBase,side1,side2,height)
            print(f"\nThe Area= {myTrapezoid.areaValue} \nThe Perimeter= {myTrapezoid.perimeterValue} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findTrapezoid()
    def findParallelogram(self):
        try:
            base = float(input("\nTo Calculate The Area And The Perimeter Of The Parallelogram..\nPlease Enter The Base Of The Parallelogram: "))
            sleep(0.3)
            side = float(input("\nPlease Enter The Side Of The Parallelogram: "))
            sleep(0.3)
            height = float(input("\nPlease Enter The Height  Of The Parallelogram: "))
            sleep(0.3)
            myParallelogram = Parallelogram(base,side,height)
            print(f"\nThe Area= {myParallelogram.areaValue} \nThe Perimeter={myParallelogram.perimeterValue} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findParallelogram()
    def findRhombus(self):
        try:
            side = float(input("\nTo Calculate The Area And The Perimeter Of The Rhombus..\nPlease Enter The Side Of The Rhombus: "))
            sleep(0.3)
            longdiagonal = float(input("\nPlease Enter The Longdiagonal Of The Rhombus: "))
            sleep(0.3)
            shortdiagonal = float(input("\nPlease Enter The Shortdiagonal  Of The Rhombus: "))
            sleep(0.3)
            myRhombus = Rhombus(side,longdiagonal,shortdiagonal)
            print(f"\nThe Area= {myRhombus.areaValue} \nThe Perimeter={myRhombus.perimeterValue} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findRhombus()
    def findRectangle(self):
        try:
            lenght = float(input("\nTo Calculate The Area And The Perimeter Of The Rectangle..\nPlease Enter The Lenght Of The Rectangle: "))
            sleep(0.3)
            width = float(input("\nPlease Enter The Width Of The Rectangle: "))
            sleep(0.3)
            myRectangle = Rectangle(lenght,width)
            print(f"\nThe Area= {myRectangle.areaValue} \nThe Perimeter={myRectangle.perimeterValue} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findRectangle()
    def findSquare(self):
        try:
            side = float(input("\nTo Calculate The Area And The Perimeter Of The Square..\nPlease Enter The Side Of The Square: "))
            sleep(0.3)
            mySquare = Square(side)
            print(f"\nThe Area= {mySquare.areaValue} \nThe Perimeter={mySquare.perimeterValue} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findSquare()
    def findPentagon(self):
        try:
            sideLength = float(input("\nTo Calculate The Area And The Perimeter Of The Regular Polygon..\nPlease Enter The Side Length Of The Regular Polygon: "))
            sleep(0.3)
            apothem = float(input("\nPlease Enter The apothem..\n(The Perpendicular Distance Between The Center Of The Polygon): "))
            sleep(0.3)
            myPentagon = Pentagon (sideLength,apothem)
            print(f"\nThe Area= {myPentagon.areaValue} \nThe Perimeter={myPentagon.perimeterValue} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findPentagon()
    def findHexagon(self):
        try:
            sideLength = float(input("\nTo Calculate The Area And The Perimeter Of The Regular Polygon..\nPlease Enter The Side Length Of The Regular Polygon: "))
            sleep(0.3)
            apothem = float(input("\nPlease Enter The apothem..\n(The Perpendicular Distance Between The Center Of The Polygon): "))
            sleep(0.3)
            myHexagon = Hexagon(sideLength,apothem)
            print(f"\nThe Area= {myHexagon.areaValue} \nThe Perimeter={myHexagon.perimeterValue} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findHexagon()
    def findOctagon(self):
        try:
            sideLength = float(input("\nTo Calculate The Area And The Perimeter Of The Regular Polygon..\nPlease Enter The Side Length Of The Regular Polygon: "))
            sleep(0.3)
            apothem = float(input("\nPlease Enter The apothem..\n(The Perpendicular Distance Between The Center Of The Polygon): "))
            sleep(0.3)
            myOctagon = Octagon(sideLength,apothem)
            print(f"\nThe Area= {myOctagon.areaValue} \nThe Perimeter={myOctagon.perimeterValue} \n")
        except:
            print("\nINVAILD INPUT!,Please Try Again")
            self.findOctagon()
    def loop(self):
        self.notExit=True
        while self.notExit:
            self.welcomeInfo()
            self.findPolygon(self.getInput())
            try:
                exitChoice = int(input("\nDo You Want To Calculate The Area And The Perimeter Another Time..\nYes! Enter 1\nNo!  Enter 2\nPlease Enter Your Choice: "))
                if exitChoice==1:
                    continue
                elif exitChoice== 2:
                    print("\nTHE END!")
                    self.notExit=False
                    break
            except:
                print("\nINVAILD INPUT!,Please Try Again")
FindTheShape()