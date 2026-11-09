

# library mangement system


books = []
borrowed_books = []

def add_book(book_name):
    if book_name == "":
        print("Book name cannot be empty")
    elif book_name in books or book_name in borrowed_books:
        print("Book already exists")
    else:
        books.append(book_name)
        print("Book added successfully")


def view_books():
    if not books:
        print("No books available")
    else:
        print("Available Books:")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book}" )

def search_book(book_name):
    if book_name == "":
        print("Please enter a book name")
    elif book_name in books:
        print(f"{book_name} - Book found")
    elif book_name in borrowed_books:
        print(f"{book_name} - Currently borrowed")
    else:
        print("Book not found")

def borrow_book(book_name):
    if book_name == "":
        print("Please enter a book name")
    elif book_name in books:
        books.remove(book_name)
        borrowed_books.append(book_name)
        print("Book borrowed successfully")
    else:
        print("Book not available")


def return_book(book_name):
    if book_name == "":
        print("Please enter a book name")
    elif book_name in borrowed_books:
        borrowed_books.remove(book_name)
        books.append(book_name)
        print("Book returned successfully")
    else:
        print("This book was not borrowed")


def view_borrowed_books():
    if len(borrowed_books) == 0:
        print("No borrowed books")
    else:
        print("Borrowed Books")
        for index , book in enumerate(borrowed_books, start= 1):
            print(f"{index}. {book}")



def main():
    print("Welcome to Library Management System")
    while True:
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View borrowed book")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name_book = input("Enter the book name: ").strip().lower()
            add_book(name_book)

        elif choice == "2":
            view_books()


        elif choice == "3":
            name_book = input("Enter book name to search: ").strip().lower()
            search_book(name_book)

        elif choice == "4":
            name_book = input("Enter book name to borrow: ").strip().lower()
            borrow_book(name_book)


        elif choice == "5":
            name_book = input("Enter return book name: ").strip().lower()
            return_book(name_book)

        elif choice == "6":
            view_borrowed_books()

        elif choice == "7":
            print("Thank you for visiting library!")
            break

        else:
            print("Invalid choice")



main()