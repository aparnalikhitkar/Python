


from abc import ABC

class Shape(ABC):
   # @abstartclassmethod()
    def area(self, a, b):
        pass


class Triangle:
    def area(self, l, b):
        return l * b


class Square(Shape()):
    def show():
        print("Welcome  in square class")


Tobj = Triangle()
print(Tobj,area(4, 5))
squareobj = Square()
shobj = Shape(3,4)