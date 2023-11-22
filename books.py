class Book:
    list_of_books = []

    # New class Book
    def __init__(self, isbn, title, cover_format, subject, rental_price_per_day, copies):
        self.isbn = isbn
        self.title = title
        self.cover_format = cover_format
        self.subject = subject
        self.rental_price_per_day = rental_price_per_day
        self.copies = copies

    # For displaying class attributes as strings
    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Cover Format: {self.cover_format}, " \
                f"Subject: {self.subject}, Rental price per day: {self.rental_price_per_day}, Copies: {self.copies}"

    # Function for adding a new book
    def add_book(self):
        new_isbn = input("Enter ISBN of the book: ")
        new_title = input("Enter title of the book: ")
        new_cover_format = input("Enter format of the book [Hardcover/Paperback]: ")
        new_subject = input("Enter subject of the book [Science/History/Literature]: ")
        new_rental_price_per_day = float(input("Enter rental price per day: "))
        new_copies = int(input("Enter no of copies: "))

        new_book = Book(new_isbn, new_title, new_cover_format, new_subject, new_rental_price_per_day, new_copies)

        self.list_of_books.append(new_book)
        print("Book added successfully!")

    # Function for removing a book
    def remove_book(self):
        book_title = input("Enter title of the book to remove: ")
        for book in self.list_of_books:
            if book.title == book_title:
                self.list_of_books.remove(book)
                print(f"{book.title} has been removed from the library")

    # Function for viewing currently available books
    def view_current_books(self):
        for book in self.list_of_books:
            if book.copies != 0:
                print(f"ISBN: {book.isbn}, Title: {book.title}, Format: {book.cover_format}, Subject: {book.subject}, "
                      f"Rental Price Per Day: {book.rental_price_per_day}, Copies: {book.copies}")

    # Function for viewing currently unavailable books
    def view_currently_unavailable_books(self):
        for book in self.list_of_books:
            if book.copies == 0:
                print(f"ISBN: {book.isbn}, Title: {book.title}, Format: {book.cover_format}, Subject: {book.subject}, "
                      f"Rental Price Per Day: {book.rental_price_per_day}, Copies: {book.copies}")

    # Function for lending a book
    def lend_book(self):
        lend_title = str(input("Enter the title of the book to lend: "))
        book_found = False
        for book in self.list_of_books:
            if book.title == lend_title:
                book.copies -= 1
                print(f"{book.title} lent successfully!")
                book_found = True
                break
        if not book_found:
            print("Book is not available!")

    # Function for returning a book
    def return_book(self):
        update_title = input("Enter the title of the book to return: ")
        book_found = False
        for book in self.list_of_books:
            if book.title == update_title:
                book.copies += 1
                print(f"{book.title} returned successfully!")
                book_found = True
                break
            if not book_found:
                print("Book is not available!")


# Creating instances of class Book
book1 = Book(isbn="ISBN1234", title="The Solar System", cover_format="Hardcover", subject="Science",
             rental_price_per_day=15.0, copies=5)
book2 = Book(isbn="ISBN9876", title="Types of Animal Species", cover_format="Paperback", subject="Science",
             rental_price_per_day=10.00, copies=8)
book3 = Book(isbn="ISBN1290", title="Second World War", cover_format="Hardcover", subject="History",
             rental_price_per_day=12.50, copies=1)

# Adding and saving instances of Book class in a list
Book.list_of_books.append(book1)
Book.list_of_books.append(book2)
Book.list_of_books.append(book3)
