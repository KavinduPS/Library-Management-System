class EducationalDVD:
    list_of_educational_dvds = []

    def __init__(self, number, title, subject, rental_price_per_day, copies):
        self.number = number
        self.title = title
        self.subject = subject
        self.rental_price_per_day = rental_price_per_day
        self.copies = copies

    def __str__(self):
        return f"DVD Number: {self.number}, Title: {self.title}, Subject: {self.subject}, " \
               f"Rental price per day: {self.rental_price_per_day}, Copies: {self.copies}"

    def add_dvd(self):
        new_dvd_number = input("Enter new DVD number: ")
        new_title = input("Enter title of the DVD: ")
        new_subject = input("Enter subject of the DVD [Astronomy/Math/Technology]: ")
        new_rental_price_per_day = float(input("Enter rental price per day: "))
        new_copies = int(input("Enter no of copies: "))

        new_dvd = EducationalDVD(new_dvd_number, new_title, new_subject, new_rental_price_per_day, new_copies)

        self.list_of_educational_dvds.append(new_dvd)
        print("Educational DVD added successfully!")

    def remove_dvd(self):
        dvd_title = input("Enter title of the DVD to remove: ")
        for dvd in self.list_of_educational_dvds:
            if dvd.title == dvd_title:
                self.list_of_educational_dvds.remove(dvd)
                print(f"{dvd.title} has been removed from the library")

    def view_current_dvds(self):
        for dvd in self.list_of_educational_dvds:
            if dvd.copies != 0:
                print(f"DVD number: {dvd.number}, Title: {dvd.title}, Subject: {dvd.subject}, "
                      f"Rental Price Per Day: {dvd.rental_price_per_day}, Copies: {dvd.copies}")

    def view_currently_unavailable_dvds(self):
        for dvd in self.list_of_educational_dvds:
            if dvd.copies == 0:
                print(f"DVD number: {dvd.number}, Title: {dvd.title}, Subject: {dvd.subject}, "
                      f"Rental Price Per Day: {dvd.rental_price_per_day}, Copies: {dvd.copies}")

    def lend_dvd(self):
        lend_title = input("Enter the title of the DVD to lend: ")
        dvd_found = False
        for dvd in self.list_of_educational_dvds:
            if dvd.title == lend_title:
                dvd.copies -= 1
                print(f"{dvd.title} lent successfully!")
                dvd_found = True
                break
            if not dvd_found:
                print("Educational DVD is not available!")

    def return_dvd(self):
        update_title = input("Enter the title of the DVD to return: ")
        dvd_found = False
        for dvd in self.list_of_educational_dvds:
            if dvd.title == update_title:
                dvd.copies += 1
                print(f"{dvd.title} returned successfully!")
                dvd_found = True
                break
            if not dvd_found:
                print("Educational DVD is not available!")


dvd1 = EducationalDVD(number="10", title="Birth of the Solar System", subject="Astronomy",
                      rental_price_per_day=2.50, copies=10)
dvd2 = EducationalDVD(number="11", title="Pythagoras Theorem", subject="Math",
                      rental_price_per_day=1.00, copies=50)
dvd3 = EducationalDVD(number="12", title="Anatomy of Body", subject="Science",
                      rental_price_per_day=2.00, copies=20)

EducationalDVD.list_of_educational_dvds.append(dvd1)
EducationalDVD.list_of_educational_dvds.append(dvd2)
EducationalDVD.list_of_educational_dvds.append(dvd3)