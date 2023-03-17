class Car:
    def __init__(self,color,model,makeYear,fuelType):
        self.color=color
        self.model=model
        self.makeYear=makeYear
        self.fuelType=fuelType

    def __str__(self):
        return "({},{},{},{})".format(self.color,self.model,self.makeYear,self.fuelType)
MERCEDES=Car('red','mercedes',2015,'gas')
BMW=Car('blue','BMW',2013,'gas')
AUDI=Car('orange','AUDI',2009,'DISEL')
print(MERCEDES)
print(BMW)
print(AUDI)