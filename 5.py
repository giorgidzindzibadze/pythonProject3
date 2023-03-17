class Bank_Account:
    def __init__(self,account_name,balance=0):
        self.__acount_name=account_name
        self.__balance=balance

    def get_name(self):
        return self.__acount_name
    def set_name(self,text):
        self.__acount_name=text
    def deposit(self):
        self.__balance=input('რამდენი გაქვს ანგარიშზე?')
        x= int(self.__balance) + int(input('რა რაოდენობის თანხა შეგაქ?'))
        print('ბალანსზე არსებული თანხაა ' + str(x))


    def withdraw(self):
        self.__balance = input('რამდენი გაქვს ანგარიშზე?')
        z= int(self.__balance) - int(input('რა რაოდენობის თანხა გაგაქ?'))
        print('ბალანსზე არსებული თანხაა ' + str(z))


    secret=property(get_name,set_name)


giorgi=Bank_Account(input('შეიტანეთ კლიენტის სახელი გვარი '))
y=int(input('შეიტანეთ შესაბამისი კოდი რომელი ოპერაციის შესრულება გსურთ:\nთანხის შეტანა:1, თანხის გამოტანა:2'))
if y==1:
    print(giorgi.deposit())
elif y==2:
    print(giorgi.withdraw())
else:
    print('შეიყვანეთ 1 ან 2')






