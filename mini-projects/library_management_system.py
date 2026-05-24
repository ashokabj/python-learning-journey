library = {
    "Python Basics": "Available",
    "AI for Beginners": "Available",
    "Data Science 101": "Available",
    "Atomic habits": "Available"
}

borrowed_books = []

while True:

    print("\n===== Library Management System =====")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nAvailable Books:")
        for book, status in library.items():
            print(f"{book} --> {status}")

    elif choice == "2":

        book_name = input("Enter book name to borrow: ")

        if book_name in library:

            if library[book_name] == "Available":
                library[book_name] = "Borrowed"
                borrowed_books.append(book_name)

                print("Book borrowed successfully ")

            else:
                print("Book is already borrowed ")

        else:
            print("Book not found ")

    elif choice == "3":

        return_book = input("Enter book name to return: ")

        if return_book in borrowed_books:

            library[return_book] = "Available"
            borrowed_books.remove(return_book)

            print("Book returned successfully ")

        else:
            print("This book was not borrowed ")

    elif choice == "4":

        print("\n========== Final Library Status ==========")

        print("\nAvailable Books:")
        for book,status in library.items():
            print(f"{book} --> {status}")

        print("\nBorrowed Books:")

        if borrowed_books:
            for book in borrowed_books:
                print(f"- {book}")

        else:
            print("No books borrowed")

        print("Thank you for using the Library Management System")
        break

    else:
        print("Invalid Choice ")