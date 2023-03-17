import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return '({},{})'.format(self.x, self.y)
    def method(x1,y1,x2,y2):
        return math.sqrt((int(x2)-int(x1))**2 + (int(y2)-int(y1))**2 )




x1=int(input('შეიყვანეთ x1'))
y1= int(input('შეიყვანეთ y1'))
x2=int(input('შეიყვანეთ x2'))
y2=int(input('შეიყვანეთ y2'))
a=Point(x1,y1)
b=Point(x2,y2)
print(Point.method(x1, y1, x2, y2))
print(a)
