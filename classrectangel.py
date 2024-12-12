class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

        def area(self):
            return self.length * self.breadth
        
        def perimeter(self):
            return 2*(self.length + self.breadth)
        
        def display(self):
            print(f"Area of Rectangel:{self.area()}")
            print(f"Perimeter of Rectangel:{self.perimeter()}")

        def compare_area(self,other):
            if self.area()==other.area():
                print("\nRectangle are equal in Area")
            elif self.area()>other.area():
                print("\nRectangle 1 is greater in area than Rectangle 2.")
            else:
                print("\nRectangle 2 is greater in area than Rectangel 1.")

print("Enter Dimensions of the first Rectangle")
length1=int(input("Enter length1:"))
breadth1=int(input("Enter Breadth1:"))
rect1=Rectangle(length1,breadth1)
rect1.display()

print("Enter Dimensions of the first Rectangle")
length2=int(input("Enter length2:"))
breadth2=int(input("Enter Breadth2:"))
rect2=Rectangle(length2,breadth2)
rect2.display()
rect1.compare_area(rect2)