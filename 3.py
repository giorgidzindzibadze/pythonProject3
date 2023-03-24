class Contacts:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone



class MailSender:

    def __init__(self,email):
        self.email=email
    def send_mail(self):
        print(f'თქვენი მეილი გაიგზავნა ამ მისამართზე:{self.email}')



class Friend(Contacts,MailSender):
    def __init__(self,name,phone,email):
        super().__init__(name,phone)
        #super().__init__(email)
        self.email=email

class Family(Contacts,MailSender):
    def __init__(self,name,phone,email,birthdate):
        super().__init__(name,phone)
        #super().__init__(email)
        self.birthdate=birthdate
        self.email=email



ka=Family('giorgi', 59926565 ,'giorgi.dzindzibadze@gmail.com','03/12/2003')
ka.send_mail()
sa=Friend('kosta',599595959,'kosta.davitashvili@gmail.com')
sa.send_mail()