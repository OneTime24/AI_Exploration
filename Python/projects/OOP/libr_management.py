class Book:
    totalcount = 0

    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.borrowed = False
        Book.totalcount += 1

    def borrow_book(self):
        if self.borrowed:
            print(f'"{self.title}" is already borrowed.')
        else:
            self.borrowed = True
            print(f'You borrowed "{self.title}".')

    def return_book(self):
        if not self.borrowed:
            print(f'"{self.title}" was not borrowed.')
        else:
            self.borrowed = False
            print(f'You returned "{self.title}".')

    @classmethod
    def display_total_book(cls):
        print(f"Total Books: {cls.totalcount}")

    @staticmethod
    def rules_library():
        print("Library Rules:")
        print("- Keep a healthy and quiet environment.")
        print("- Return books on time.")
        print("- Handle books with care.\n")

    def display(self):
        status = "Borrowed" if self.borrowed else "Available"
        print(f"Title: {self.title} | Author: {self.author} | Status: {status}")

    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"


class Ebook(Book):
    def __init__(self, author, title, size):
        super().__init__(author, title)
        self.size = size

    def display(self):
        status = "Borrowed" if self.borrowed else "Available"
        print(
            f"Title: {self.title} | Author: {self.author} | "
            f"Size: {self.size} | Status: {status}"
        )


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" added to library.')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'"{book.title}" removed from library.')
        else:
            print("Book not found.")

    def show_books(self):
        if not self.books:
            print("No books found.")
            return

        print("\n------ Library Books ------")
        for book in self.books:
            book.display()
        print()

    def search(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("\nBook Found:")
                book.display()
                return

        print("No book found with that title.")


# ------------------ Driver Code ------------------

lib = Library()

b1 = Book("Jeffry", "How to Survive")
b2 = Book("Fredrik Backman", "A Man Called Ove")
b3 = Ebook("James Clear", "Atomic Habits", "5 MB")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print()

lib.show_books()

Book.display_total_book()
print()

Book.rules_library()

b1.borrow_book()
print()

lib.show_books()

lib.search("Atomic Habits")
print()

b1.return_book()
print()

lib.remove_book(b2)
print()

lib.show_books()

Book.display_total_book()