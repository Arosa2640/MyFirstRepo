import math
class Shape:

    def area(self):

        pass

    def perimeter(self):

        pass

class Rectangle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        return math.pi * self.radius ** 2

    def perimeter(self):

        return 2 * math.pi * self.radius


class Triangle(Shape):

    def __init__(self, length, width):

        self.length = length

        self.width = width

    def area(self):

        return self.length * self.width

    def perimeter(self):

        return 2 * (self.length + self.width)


class Circle(Shape):

    def __init__(self, a, b, c):

        self.a = a

        self.b = b

        self.c = c

    def area(self):

        s = (self.a + self.b + self.c) / 2

        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):

        return self.a + self.b + self.c


while True:

    print("\n1.Rectangle  2.Triangle  3.Circle  4.Exit")

    option = input("Pick: ")

    try:

        if option == "1":

            shape = Circle(float(input("Radius: ")))

        elif option == "2":

            shape = Rectangle(

                float(input("Length: ")),

                float(input("Width: "))

            )

        elif option == "3":

            shape = Triangle(

                float(input("Side A: ")),

                float(input("Side B: ")),

                float(input("Side C: "))

            )

        elif option == "4":

            break

        else:

            continue

        print("Area:", shape.area())

        print("Perimeter:", shape.perimeter())

    except:

        print("Numbers only")
 