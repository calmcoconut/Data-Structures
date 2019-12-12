# -*- coding: utf-8 -*-
"""
Author: Alejandro Diaz
8/24/2019

Develop the classes Book and Patron
with the following characteristics:
A patron can have at most three books out on loan at any given time. 
A book also has a list of patrons waiting to borrow it. 
Each book has a title, an author, a patron to whom it has been checked out, 
and a list of patrons waiting for that book to be returned. 
Each patron has a name and the number of books it has currently checked out.
    
Checkout feature and waitlist feature as outlined by the instructions.
To improve I was add queue functionality for the waitlist.

Input: book that is added to the library; Patron that is a part of the library.
.borrow(patron) to borrow
.addBook(book) to add book

Output: using str(book) describes who has checked out the book as well as how many books they hold
        str(patron) describes the person's name and number of books checked out
        waitList() function describes the state of the waitlist.
    
"""

class Book:
    library_members = {}
    waiting = {}
    members_waiting = []
    book_list = []
    
    def __init__(self, tittle, author, status= 1, borrowed_to = ''):
        self.tittle = tittle
        self.author = author
        self.status = status
        self.borrowed_to = borrowed_to
        self.waiting_list = []
        self.catalog = [author + ", " + tittle]
        self.book_list.append(self)
        Book.library_members = Book.library_members

    
    def borrow(self, borrower):
        if self.status == 1:            
            self.borrowed_to = borrower.name            
            if self.catalog not in borrower.holding:
                borrower.holding.append(self.catalog)
            else:
                self.status = 0
        elif self.status == 0:
            Book.members_waiting.append(borrower.name)
            self.waiting_list.append(borrower.name)
        else:
            print('error')
            return "error"
            
    def __str__(self):
        return str(self.tittle + ", " + self.author + " in care of: " + self.borrowed_to + " has " + str(self.library_members[self.borrowed_to]) + " books \n")
    
class Patron:
    patron_list = []
    def __init__(self,name,book=0):
        self.name = name
        self.book = book
        self.holding = []
        Book.library_members = Book.library_members
        Book.waiting = Book.waiting
        Book.members_waiting = Book.members_waiting
        self.newMember()
        self.patron_list.append(self)
    
    def newMember(self):
        Book.library_members.update({self.name : self.book})
        Book.waiting.update({self.name : self.book})
    
    def addBook(self, adding):
        """ 
        Adds book to patron. First checks if max checkout books is reached (3 books).
        Then checks if book is available. if not available will add to wait list.
        """
        if self.book >= 3:
            print("Can't borrow more books--MAX REACHED!\n")
            return "Can't borrow more books--MAX REACHED!"
#        elif adding.status == 0:
#            wait_list()
        elif adding.status == 1 and self.book < 3:
            self.book = self.book + 1
            if adding.catalog not in self.holding:
                self.holding.append(adding.catalog)
            else:
                adding.status = 0
            Book.library_members[self.name] = self.book
            Book.waiting[self.name] = Book.library_members[self.name]
            return self.holding
        elif adding.status == 0:
            Book.members_waiting.append(self.name)
            Patron.waitList()
        else:
            return "error. cannot add"
        
    def __str__(self):
        return str(self.name + " has " + str(self.book) + " books")

def waitList():
    if len(Book.members_waiting) > 0:
        Book.members_waiting = set(Book.members_waiting)
        print("Waiting:")
        count = 1
        for name in Book.members_waiting:
            print(str(count) +". " + name + " has "+ str(Book.waiting[name]) + " books")
            count += 1
        print("")
    return Book.members_waiting

def main():
    book1 = Book("Of Mice and Men", "Steinbeck")
    book2 = Book("The Great Gatsby", "Fitzgerald")
    book3 = Book("1984", "Orwell")
    book4 = Book("One Flew Over the Cuckoo's Nest", "Kesey")
    
    patron1 = Patron("Ivan")
    patron2 = Patron("Jimmy")
    patron3 = Patron("Bob")
    
    book1.borrow(patron1)
    patron1.addBook(book1)
    
    book1.borrow(patron2)
    book1.borrow(patron3)
    book2.borrow(patron1)
    patron1.addBook(book2)
    book3.borrow(patron1)
    patron1.addBook(book3)
    patron1.addBook(book4)
    book4.borrow(patron2) #triggers wait list
    patron2.addBook(book4)
    
    print("Book1 : " + str(book1))
    waitList()
    print("Patron1: " + str(patron1))
    print(Book.library_members)

if __name__ == '__main__':
    main()
