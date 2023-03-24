import random
class LibraryItem:
    def __init__(self,title, subject,status):
        self.title=title
        self.subject=subject
        self.status=status
        y=['available','occupied']
        self.status=random.choice(y)
        #if status == 'available' == bool(1) or status == 'occupied' == bool(0):
           # self.status = status
    def booking(self):
        if self.status == 'available' :
            print('თქვენ წარმატებით დაჯავშნეთ ნივთი')
        elif self.status == 'occupied' :
            print('სამწუხაროდ თქვენ ვერ დაჯავშნეთ ნივთი')

class Book(LibraryItem):
    def __init__(self,title,subject,status,ISBN,authors,):
        super().__init__(title,subject,status)
        self.ISBN=ISBN
        self.authors=authors

    def booking(self):
        if self.status == 'available' :
            print(f'თქვენ წარმატებით დაჯავშნეთ ნივთი, ISBN:{self.ISBN}, ავტორი:{self.authors}')
        elif self.status == 'occupied' :
            print('არჩეული ნივთი დაკავებულია, სამწუხაროდ თქვენ ვერ დაჯავშნეთ!')


class Cd(LibraryItem):
    def __init__(self,title,status):
        super().__init__(title,'',status)
    def booking(self):
        print( 'cd-ის დაჯავშნა არ შეიძლება')






k=LibraryItem('ნუ მოკლავ ჯაფარას','წიგნი (რომანი)',1)
k.booking()
l=Book('ძმები კარამაზოვები','წიგნი (რომანი)',1,4545,'ფიოდორ დოსტოევსკი')
l.booking()
Arctic_Monkeys=Cd('am',1)
Arctic_Monkeys.booking()
