import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def method(self):
        return math.sqrt(int(self.x*self.x)+int(self.y*self.y))

# ინფუთით დავტოვე საბოლოოდ
#point1=Point(3,5)
#point2=Point(6,9)
point3=Point(int(input('შეიყვანეთ x')),int(input('შეიყვანეთ y')))
#print(point1.method())
#print(point2.method())
print(point3.method())
