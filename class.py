#Library management system
class Library:
    def __init__(self,listofbooks):
        self.availablebooks = listofbooks
        self.borrwedbooks = []
    def displayAvailablebooks(self):
        print("The books available right now are as follows:")
       
        for book in self.availablebooks:
            print(book)
    def lendbooks(self,i):
        if i in self.availablebooks:
            print("You have borrowed book!")
            self.availablebooks.remove(i)
            self.borrwedbooks.append(i)

        else:
            print("Sorry!The book you requested for is not in stock at the moment")
    def Returned(self,i):
        print("Book returned successfully ")
        self.availablebooks.append(i)
        self.borrwedbooks.remove(i)
    def displayBorrow(self):
        if(self.borrwedbooks==[]):
            print("You haven't yet borrowed any books")
        else:
            print("The list of books that you have borrowed is:")
            for i in self.borrwedbooks:
                print(i)
class Student:
    def borrowbook(self):
        print("Enter the name of the book you would like to borrow:")
        self.book = input()
        return self.book
    def returnbook(self):
        print("Enter the name of the book you would like to return:")
        self.book = input()
        return self.book
def main():
    library=Library(["Harry Potter and The Goblet of Fire","Harry Potter and the Prisoners of Azkaban","Atomic Habits","The Power of subconcious mind","Autobiography of Yogi"])
    student= Student()
    
    flag = False
    while (flag == False):
        print(""" =======LIBRARY MENU==========
            1. Display All Available Books
            2. Request A Book
            3. Return A Book
            4. Show books that I have borrowed
            5. Exit""")
        choice=int(input("Enter your choice"))
        if(choice ==1):
            library.displayAvailablebooks()
        if(choice==2):
            library.lendbooks(student.borrowbook())
        if(choice==3):
            library.Returned(student.returnbook())
        if(choice==4):
            library.displayBorrow()
        if(choice==5):
            sys.exit()
main()


