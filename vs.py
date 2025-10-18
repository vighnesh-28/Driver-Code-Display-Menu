class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"{self.title} by {self.author} [{status}]"


class Library:
    def __init__(self, name):
        self.library_name = name
        self.books = []

    def display_books(self):
        if not self.books:
            print("\nNo books available in the library!\n")
        else:
            print(f"\nBooks in {self.library_name}:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")
            print()

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"'{title}' by {author} has been added to the library.\n")

    def borrow_book(self, title, student_name):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"'{title}' has been borrowed by {student_name}.\n")
                else:
                    print(f"'{title}' is already borrowed by another student.\n")
                return
        print(f"Book '{title}' not found in the library.\n")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"'{title}' has been returned successfully.\n")
                else:
                    print(f"'{title}' was not borrowed.\n")
                return
        print(f"Book '{title}' not found in the library.\n")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"'{title}' has been removed from the library.\n")
                return
        print(f"Book '{title}' not found in the library.\n")


def main():
    library = Library("Student Central Library")

    while True:
        print("====== Library Menu ======")
        print("1. Display all books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Remove a book")
        print("6. Exit")
        print("==========================")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            title = input("Enter the name of the book: ")
            author = input("Enter the author name: ")
            library.add_book(title, author)
        elif choice == '3':
            title = input("Enter the name of the book to borrow: ")
            student_name = input("Enter the student's name: ")
            library.borrow_book(title, student_name)
        elif choice == '4':
            title = input("Enter the name of the book to return: ")
            library.return_book(title)
        elif choice == '5':
            title = input("Enter the name of the book to remove: ")
            library.remove_book(title)
        elif choice == '6':
            print("Exiting the Library System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
