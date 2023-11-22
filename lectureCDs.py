class LectureCD:
    list_of_lecture_cds = []

    def __init__(self, number, title, subject, rental_price_per_day, copies):
        self.number = number
        self.title = title
        self.subject = subject
        self.rental_price_per_day = rental_price_per_day
        self.copies = copies

    def __str__(self):
        return f"CD Number: {self.number}, Title: {self.title}, Subject: {self.subject}, " \
               f"Rental price per day: {self.rental_price_per_day}, Copies: {self.copies}"

    def add_cd(self):
        new_cd_number = input("Enter new CD number: ")
        new_title = input("Enter title of the CD: ")
        new_subject = input("Enter subject of the CD [Music/Math/Foreign Languages]: ")
        new_rental_price_per_day = float(input("Enter rental price per day: "))
        new_copies = int(input("Enter no of copies: "))

        new_cd = LectureCD(new_cd_number, new_title, new_subject, new_rental_price_per_day, new_copies)

        self.list_of_lecture_cds.append(new_cd)
        print("Lecture CD added successfully!")

    def remove_cd(self):
        cd_title = input("Enter title of the CD to remove: ")
        for cd in self.list_of_lecture_cds:
            if cd.title == cd_title:
                self.list_of_lecture_cds.remove(cd)
                print(f"{cd.title} has been removed from the library")

    def view_current_cds(self):
        for cd in self.list_of_lecture_cds:
            if cd.copies != 0:
                print(f"CD number: {cd.number}, Title: {cd.title}, Subject: {cd.subject},"
                      f"Rental Price Per Day: {cd.rental_price_per_day}, Copies: {cd.copies}")

    def view_currently_unavailable_cds(self):
        for cd in self.list_of_lecture_cds:
            if cd.copies == 0:
                print(f"CD number: {cd.number}, Title: {cd.title}, Subject: {cd.subject},"
                      f"Rental Price Per Day: {cd.rental_price_per_day}, Copies: {cd.copies}")

    def lend_cd(self):
        lend_title = input("Enter the title of the CD to lend: ")
        cd_found = False
        for cd in self.list_of_lecture_cds:
            if cd.title == lend_title:
                cd.copies -= 1
                print(f"{cd.title} lent successfully!")
                cd_found = True
                break
            if not cd_found:
                print("Lecture CD is not available!")

    def return_cd(self):
        update_title = input("Enter the title of the CD to return: ")
        cd_found = False
        for cd in self.list_of_lecture_cds:
            if cd.title == update_title:
                cd.copies += 1
                print(f"{cd.title} returned successfully!")
                cd_found = True
                break
            if not cd_found:
                print("Lecture CD is not available!")


cd1 = LectureCD(number="21", title="Basics of Western Music", subject="Music",
                rental_price_per_day="1.50", copies=11)
cd2 = LectureCD(number="22", title="Japanese Language", subject="Foreign Languages",
                rental_price_per_day="2.00", copies=3)
cd3 = LectureCD(number="23", title="Space Science", subject="Science",
                rental_price_per_day="5.00", copies=6)

LectureCD.list_of_lecture_cds.append(cd1)
LectureCD.list_of_lecture_cds.append(cd2)
LectureCD.list_of_lecture_cds.append(cd3)