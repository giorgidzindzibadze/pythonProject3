class Celsius:
    def __init__(self,temperature):
        self.__temperature=temperature

    def get_temp(self):
        return self.__temperature
    def set_temp(self,text):
        self.__text=text
    def del_temp(self):
        del self.__temperature
    temperature=property(get_temp,set_temp,del_temp)

temp1=Celsius(30)
temp1.temperature=3
temp2=Celsius(90)
del temp2
temp3=Celsius(93)
print(temp1.temperature)
print(temp3.temperature)

