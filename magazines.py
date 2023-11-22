class Magazine:
    list_of_mags = []

    def __init__(self, number, title, print_color, subject, rental_price_per_day, copies):
        self.number = number
        self.title = title
        self.print_color = print_color
        self.subject = subject
        self.rental_price_per_day = rental_price_per_day
        self.copies = copies

    def __str__(self):
        return f"Magazine Number: {self.number}, Title: {self.title}, Print Color: {self.print_color}, " \
               f"Subject: {self.subject}, Rental price per day: {self.rental_price_per_day}, Copies: {self.copies}"

    def add_mag(self):
        new_mag_number = input("Enter new magazine number: ")
        new_title = input("Enter title of the magazine: ")
        new_print_color = input("Enter color of the print [Color/Black and white]: ")
        new_subject = input("Enter subject of the magazine [Science/Technology/Sports]: ")
        new_rental_price_per_day = float(input("Enter rental price per day: "))
        new_copies = int(input("Enter no of copies: "))

        new_mag = Magazine(new_mag_number, new_title, new_print_color, new_subject, new_rental_price_per_day,
                           new_copies)

        self.list_of_mags.append(new_mag)
        print("Magazine added successfully!")

    def remove_mag(self):
        mag_title = input("Enter title of the magazine to remove: ")
        for mag in self.list_of_mags:
            if mag.title == mag_title:
                self.list_of_mags.remove(mag)
                print(f"{mag.title} has been removed from the library")

    def view_current_mags(self):
        for mag in self.list_of_mags:
            if mag.copies != 0:
                print(f"Magazine number: {mag.number}, Title: {mag.title}, Format: {mag.print_color}, "
                      f"Subject: {mag.subject},Rental Price Per Day: {mag.rental_price_per_day}, "
                      f"Copies: {mag.copies}")

    def view_currently_unavailable_mags(self):
        for mag in self.list_of_mags:
            if mag.copies == 0:
                print(f"Magazine number: {mag.number}, Title: {mag.title}, Format: {mag.print_color}, "
                      f"Subject: {mag.subject},Rental Price Per Day: {mag.rental_price_per_day}, "
                      f"Copies: {mag.copies}")

    def lend_mag(self):
        lend_title = input("Enter the title of the mag to lend: ")
        mag_found = False
        for mag in self.list_of_mags:
            if mag.title == lend_title:
                mag.copies -= 1
                print(f"{mag.title} lent successfully!")
                mag_found = True
                break
            if not mag_found:
                print("Magazine is not available!")

    def return_mag(self):
        update_title = input("Enter the title of the magazine to return: ")
        mag_found = False
        for mag in self.list_of_mags:
            if mag.title == update_title:
                mag.copies += 1
                print(f"{mag.title} returned successfully!")
                mag_found = True
                break
            if not mag_found:
                print("Magazine is not available!")


mag1 = Magazine(number="01", title="History of Cricket", print_color="color", subject="Sports",
                rental_price_per_day=5.00, copies=7)
mag2 = Magazine(number="02", title="Evolution of the Computer", print_color="black&white", subject="Technology",
                rental_price_per_day=3.00, copies=21)
mag3 = Magazine(number="03", title="Earth", print_color="black&white", subject="Science",
                rental_price_per_day=2.00, copies=15)

Magazine.list_of_mags.append(mag1)
Magazine.list_of_mags.append(mag2)
Magazine.list_of_mags.append(mag3)
