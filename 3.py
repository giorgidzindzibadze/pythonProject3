class Dog:
    def __init__(self,breed,size,age,color):
        self.breed=breed
        self.size=size
        self.age=age
        self.color=color

    def __str__(self):
        return "({},{},{},{})".format(self.breed,self.size,self.age,self.color)


dog1=Dog('Napolitan Mastiff','Large','5 years','black')
dog2=Dog('Maltese','Small','2 years','white')
dog3=Dog('Chow Chow','medium','3 years','Brown')
print(dog1)
print(dog2)
print(dog3)