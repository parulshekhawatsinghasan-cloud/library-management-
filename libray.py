class LibraryManagement:

    def __init__(self):
        self.books = []

    def main_menu(self):

        while True:
            print("\n")
            print("=" * 40)
            print("     LIBRARY MANAGEMENT SYSTEM")
            print("=" * 40)

            print("1. Add Book")
            print("2. View Books")
            print("3. Issue Book")
            print("4. Return Book")
            print("5. Delete Book")
            print("6. Exit")

            choice = input("\nEnter Choice: ")

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.view_books()

            elif choice == "3":
                self.issue_book()

            elif choice == "4":
                self.return_book()

            elif choice == "5":
                self.delete_book()

            elif choice == "6":
                print("\nThank You For Using Library System")
                break

            else:
                print("Invalid Choice")

    def add_book(self):

        name = input("Enter Book Name: ")

        self.books.append({
            "name": name,
            "issued": False
        })

        print("Book Added Successfully")

    def view_books(self):

        if len(self.books) == 0:
            print("No Books Available")
            return

        print("\nBOOK LIST\n")

        for i in range(len(self.books)):

            status = (
                "Issued"
                if self.books[i]["issued"]
                else "Available"
            )

            print(
                i + 1,
                ".",
                self.books[i]["name"],
                "-",
                status
            )

    def issue_book(self):

        self.view_books()

        if len(self.books) == 0:
            return

        try:

            num = int(
                input(
                    "Enter Book Number: "
                )
            ) - 1

            if self.books[num]["issued"]:
                print("Already Issued")

            else:
                self.books[num]["issued"] = True

                print("Book Issued")

        except:
            print("Invalid Input")

    def return_book(self):

        self.view_books()

        if len(self.books) == 0:
            return

        try:

            num = int(
                input(
                    "Enter Book Number: "
                )
            ) - 1

            self.books[num]["issued"] = False

            print("Book Returned")

        except:
            print("Invalid Input")

    def delete_book(self):

        self.view_books()

        if len(self.books) == 0:
            return

        try:

            num = int(
                input(
                    "Enter Book Number: "
                )
            ) - 1

            deleted = self.books.pop(num)

            print(
                deleted["name"],
                "Deleted"
            )

        except:
            print("Invalid Input")


library = LibraryManagement()

library.main_menu()
