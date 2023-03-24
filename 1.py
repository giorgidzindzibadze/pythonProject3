class People:
    def __init__(self,firstname, lastname):
        self.firstname=firstname
        self.lastname=lastname
    def get_email(self):
        print(f'{self.firstname}.{self.lastname}.uni@btu.edu.ge')

class Student(People):
    def __init__(self,firstname,lastname,courses):
        super().__init__(firstname,lastname)
        self.courses=courses
        self.courses=[input('შეიყვანეთ 1-ლი ლექცია'),input('შეიყვანეთ მე-2 ლექცია'),input('შეიყვანეთ მე-3 ლექცია'),
                      input('შეიყვანეთ მე-4 ლექცია'),input('შეიყვანეთ მე-5 ლექცია'),input('შეიყვანეთ მე-6 ლექცია')]


    def get_email(self):
        print(f'{self.firstname}.{self.lastname}.1@btu.edu.ge'
              f' კურსების ჩამონათვალი: {self.courses}')

class Lecturer(People):
    def __init__(self,firstname,lastname,salary):
        super().__init__(firstname,lastname)
        self.salary=salary
    def get_email(self):
        print(f'{self.firstname}.{self.lastname}.@btu.edu.ge'
              f' ანაზღაურება {self.salary}')



gio=People('giorgi','dzindzibadze')
gio.get_email()
la=Student('luka','shukakidze',5)
la.get_email()
si=Lecturer('lika','svanadze',99999)
si.get_email()
