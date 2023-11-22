from books import Book
from magazines import Magazine
from educationalDVDs import EducationalDVD
from lectureCDs import LectureCD


# main class resources
class Resources:
    list_of_books = Book.list_of_books
    list_of_mags = Magazine.list_of_mags
    list_of_dvds = EducationalDVD.list_of_educational_dvds
    list_of_cds = LectureCD.list_of_lecture_cds

    def __init__(self, book, magazine, educational_dvd, lecture_cd):
        self.book = book
        self.magazine = magazine
        self.educational_dvd = educational_dvd
        self.lecture_cd = lecture_cd

    def view_by_subject(self):
        filter_subject = str(input("Enter a subject to view all resources[Science, History, Literature, Technology,"
                                   "Sports, Astronomy, Math, Music, Foreign Languages]: "))

        for book in self.list_of_books:
            if book.subject == filter_subject:
                print(book)
        for mag in self.list_of_mags:
            if mag.subject == filter_subject:
                print(mag)
        for dvd in self.list_of_dvds:
            if dvd.subject == filter_subject:
                print(dvd)
        for cd in self.list_of_cds:
            if cd.subject == filter_subject:
                print(cd)


new_resource = Resources(book="", magazine="", educational_dvd="", lecture_cd="")
new_book = Book(isbn="", title="", cover_format="", subject="", rental_price_per_day=0, copies=0)
new_mag = Magazine(number="", title="", print_color="", subject="", rental_price_per_day=0, copies=0)
new_dvd = EducationalDVD(number="", title="", subject="", rental_price_per_day=0, copies=0)
new_cd = LectureCD(number="", title="", subject="", rental_price_per_day=0, copies=0)


def main_menu():
    print("~~~Library System~~~")
    print("Choose an option")

    main_functions = ["1. Add new resource", "2. Remove a resource", "3. View available resources",
                      "4. View unavailable resources", "5. View all resources", "6. Lend a resource",
                      "7. Update resource", "8. Exit"]

    for x in main_functions:
        print(x)


resource_types = ["1. Books", "2. Magazines", "3. Educational DVDs", "4. Lecture CDs"]


def commands():

    while True:
        main_menu()
        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Choose a resource type to add")
            for x in resource_types:
                print(x)

            resource_type = int(input("Enter choice: "))

            if resource_type == 1:
                Book.add_book(new_book)
            elif resource_type == 2:
                Magazine.add_mag(new_mag)
            elif resource_type == 3:
                EducationalDVD.add_dvd(new_dvd)
            elif resource_type == 4:
                LectureCD.add_cd(new_cd)

        elif choice == 2:
            print("Choose a resource type to remove")
            for x in resource_types:
                print(x)

            resource_type = int(input("Enter choice: "))

            if resource_type == 1:
                Book.remove_book(new_book)
            elif resource_type == 2:
                Magazine.remove_mag(new_mag)
            elif resource_type == 3:
                EducationalDVD.remove_dvd(new_dvd)
            elif resource_type == 4:
                LectureCD.remove_cd(new_cd)

        elif choice == 3:
            print("Choose a resource type to view")
            for x in resource_types:
                print(x)

            resource_type = int(input("Enter choice: "))

            if resource_type == 1:
                Book.view_current_books(new_book)
            elif resource_type == 2:
                Magazine.view_current_mags(new_mag)
            elif resource_type == 3:
                EducationalDVD.view_current_dvds(new_dvd)
            elif resource_type == 4:
                LectureCD.view_current_cds(new_cd)

        elif choice == 4:
            print("Choose a resource type to view")
            for x in resource_types:
                print(x)

            resource_type = int(input("Enter choice: "))

            if resource_type == 1:
                Book.view_currently_unavailable_books(new_book)
            elif resource_type == 2:
                Magazine.view_currently_unavailable_mags(new_mag)
            elif resource_type == 3:
                EducationalDVD.view_currently_unavailable_dvds(new_dvd)
            elif resource_type == 4:
                LectureCD.view_currently_unavailable_cds(new_cd)

        elif choice == 5:
            Resources.view_by_subject(new_resource)

        elif choice == 6:
            print("Choose a resource type to lend")
            for x in resource_types:
                print(x)

            resource_type = int(input("Enter choice: "))

            if resource_type == 1:
                Book.lend_book(new_book)
            elif resource_type == 2:
                Magazine.lend_mag(new_mag)
            elif resource_type == 3:
                EducationalDVD.lend_dvd(new_dvd)
            elif resource_type == 4:
                LectureCD.lend_cd(new_cd)

        elif choice == 7:
            print("Choose a resource type to return")
            for x in resource_types:
                print(x)

            resource_type = int(input("Enter choice: "))

            if resource_type == 1:
                Book.return_book(new_book)
            elif resource_type == 2:
                Magazine.return_mag(new_mag)
            elif resource_type == 3:
                EducationalDVD.return_dvd(new_dvd)
            elif resource_type == 4:
                LectureCD.return_cd(new_cd)

        elif choice == 8:
            print("Thanks for using library system! Exiting...")
            return 0


commands()

