


class Book:

    totalcount=0
    def _init__(self, author, title):

        self.author=author
        self.title=title
        self.borrowed=False

        Book.totalcount+=1

    
    def borrow_book(self):
        self.borrowed=True

    def return_book(self):
        self.borrowed=False

    
    @classmethod
    def display_total_book(cls):
        print(f"Total Books: {cls.totalcount}")

    @staticmethod

    def rules_librarry():
        print("Keep a healthy and quiet environment: ")

    def display(self):

        print(f"Book Title: {self.title} | Author: {self.author}")


class Ebook:

    def __init__(self,author,title,size):
        super().__init__(author,title)
        self.size=size

    
    def display(self):

        print(f"Book Title: {self.title} | Author: {self.author} | Size: {self.size}")




class library:

    def __init__(self):

        self.books=[]

    def add_book(self,book):

        self.books.append(book)

    def remove_book(self,book):

        if book not in self.books:
            print("Book not found: ")
        else:

            self.books.pop(book)

    
    def show_books(self):

        if not self.books:
            print("No books found: ")
            return

        
        for book in self.books:
            print(book)

    
    def search(self,title):

        for book in self.books:
            if book.title.lower()==title.lower():
                print(book)
                return
            
            print("No Books Found: ")



lib=library()

b1=Book("Jeffry","How to survive")
b2=Book("A man called ove","fredrick Becjhman")
b3=Ebook("Atomic Habits","No idea")


lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

lib.show_books()

Book.display_total_book()

Book.rules_librarry()

b1.borrow_book()

print(b1)