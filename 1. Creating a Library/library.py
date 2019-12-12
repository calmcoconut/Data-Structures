# Created by Alejandro at 8/30/2019
"""
Description:
Develop a Library class that can manage the books and patrons. This class should include methods for
adding, removing, and finding books and patrons: addBook, addPatron, removeBook, removePatron, findBook, and findPatron,
respectively for each. There should also be methods for borrowing and returning a book: borrowBook and returnBook, respectively.
If you have yet to add a data member to keep track of the list of books a patron has borrowed, now would be a good time to do so.
"""
from abstract_library import Book, Patron, waitList

class Library(object):
    """
    Uses classes from an adjusted exercise1 file. aggregates these functions and describes methods that allow
    streamlined function calling.
    """
    library_patrons = Book.library_members
    library_books = []
    library_books_lis = []
    def __init__(self, books):
        self.add_to_library = self.library_books.append([book.tittle + ", " + book.author for book in books])
        Library.library_patrons = Library.library_patrons
        Library.library_books = Library.library_books
        self.library_books_lis.append(self)

    def __str__(self):
        """ returns books in library"""
        print("Books:")
        for book in Book.book_list:
            try:
                print(str(book.tittle + ", " + book.author + " in care of: " + book.borrowed_to + " has " + str(
                book.library_members[book.borrowed_to]) + " books \n"))
                print("Waiting:")
                if len(book.waiting_list>0):
                    print(book.waiting_list, book.waiting_list, Book.library_members[book.waiting_list])
            except KeyError:
                print(book.tittle + ", " + book.author + " in care of: No one")



    def returnBook(self, book, patron):
        """Allows book to be available for check out"""
        if patron.name != book.borrowed_to:
            print('book not able to be returned')
            pass
        else:
            book.borrowed_to = ""
            book.status = 1
            #patron.holding = [[i for i in nested if i != (book.author + ", " + book.tittle)] for nested in
            # patron.holding]
            patron.book = patron.book - 1
            for i, v in enumerate(patron.holding):
                if v[0] == str(book.author + ", " + book.tittle):
                    patron.holding.remove(patron.holding[i])



    def addPatron(self, patron):
        pass

    def borrowBook(self, book, patron):
        """Book is no longer available and is check out by given patron"""
        patron.addBook(book)
        book.borrow(patron)
        return 0

    def removePatron(self,patron):
        """Removes patron from the library. Will not allow patron to be removed unless they return all books."""
        if patron.book != 0:
            print("Patron must return all books!")
        else:
            del Library.library_patrons[patron.name]
            Patron.patron_list.remove(patron)
            del Book.waiting[patron.name]
            patron.name = None
            patron.book = 999
            patron.holding = None

    def removeBook(self,book):
        """Removes book from library so long as it is not checked out"""
        if book.status == 0:
            print("Book must be returned!")
        else:
            for i, v in enumerate(Library.library_books):
                if v[0] == str(book.author + ", " + book.tittle):
                    Library.library_books.remove(Library.library_books[i])
            Book.book_list.remove(book)
            tittle = None
            author = None
            status = None
            borrowed_to = None
            waiting_list = None
            catalog = None
            del self

    def findPatron(self):
        """Returns statement if input is a memeber of the library, otherwise returns None"""
        inp = str(input("Please enter patron's name"))
        if inp in Library.library_patrons:
            print(inp + "is a patron here...")

def main():
    book1 = Book('1984', 'Orwell')
    book2 = Book("The Great Gatsby", "Fitzgerald")
    books_to_add = []
    books_to_add.append(book1)
    books_to_add.append(book2)

    patron1 = Patron('Bob')
    patron2 = Patron('hoeass')

    myLibrary = Library(books_to_add)


if __name__ == '__main__':
    main()