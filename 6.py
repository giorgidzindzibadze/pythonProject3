class Fraction:
    def __init__(self,top,bottom):
        self.top=top
        self.bottom=bottom

    def __str__(self):
        return  '({}/{})'.format(self.top,self.bottom)

    def sum(self,other_fraction):
        new_num=self.top*other_fraction.bottom + self.bottom*other_fraction.top
        new_num2=self.bottom*other_fraction.bottom
        return Fraction(new_num,new_num2)
    def inverse(self):
        return Fraction(self.bottom, self.top)

    def sum1(self,other_fraction):
        new_num3=self.top+other_fraction.top
        new_num4=self.bottom
        return Fraction(new_num3,new_num4)


#აქ მინდოდა რომ გამეკეთებინა თუ ერთი მნიშვნელი ექნებოდა sum1 ით გაეკეთებინა ამ შემთხვევაში განსხვავებულ მნიშვნელიანებს აჯამებს სწორად
#if self.bottom!=other_fraction.bottom:
 #        print(gio.sum(other_fraction=lasha))
#else:
 #        print(gio.sum1(other_fraction==lasha))


gio=Fraction(3,4)
lasha=Fraction(9,6)

print(gio.sum(other_fraction=lasha))
print(gio.inverse())
print(gio)