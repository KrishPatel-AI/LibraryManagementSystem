# main.py

from library import Library
from allclasses import Book, Member, PremiumMember
import re

def main():

    library = Library()

    while True:

        print("==> This is Library Management System <==")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Show Books")
        print("4. Search Book")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Transaction History")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter Book Title: ").strip()
            if title == "":
                print("Title cannot be empty")
                continue

            author = input("Enter Book Author: ").strip()
            if author == "":
                print("Author cannot be empty")
                continue

            isbn = input("Enter Book ISBN: ").strip()
            if isbn == "":
                print("ISBN cannot be empty")
                continue

            if not int(isbn):
                print("ISBN must be valid")


            category = input ("Enter Book Category: ").strip()
            if category == "":
                print("Category cannot be empty")
                continue

            try:
                quantity = int(input("Enter Quantity: "))
                if quantity <0:
                    print("Please enter a positive integer")
                    continue

            except ValueError:
                print("Enter a valid quantity")
                continue

            book = Book(title, author, isbn, category, quantity)

            library.add_book(book)

        elif choice == "2":
            name = input("Enter Member name:").strip()
            if name == "":
                print("Member name cannot be empty")
                continue

            email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

            email = input("Enter Member email:").strip()
            if email == "":
                print("Member email cannot be empty")
                continue
            if not re.match(email_pattern, email):
                print("Enter valid email")
                continue

            memberID = input("Enter Member ID:").strip()
            if memberID == "":
                print("Member ID cannot be empty")
                continue

            member_type  = input ("Premium Member (yes or no):").strip()
            if member_type == "":
                print("Member type cannot be empty")
                continue

            if member_type.lower() == "yes":
                level = input("Enter premium level:")

                member = PremiumMember(name, email, memberID, level)

            else:
                member = Member(name, email, memberID)

            library.register_member(member)


        elif choice == "3":
            library.show_books()

        elif choice == "4":
            keyword = input("Enter Book Keyword:")

            library.search_book(keyword)

        elif choice == "5":
            memberID = input("Enter Member ID:")
            isbn = input("Enter ISBN:")

            library.issue_book(memberID, isbn)

        elif choice == "6":
            memberID = input("Enter Member ID:")
            isbn = input("Enter ISBN:")
            library.return_book(memberID, isbn)

        elif choice == "7":
            library.show_transactions()

        elif choice == "8":
            print("Thank you for using Library Management System")
            break

        else:
            print("Enter a valid choice from 1 to 8")

if __name__ == "__main__":
    main()
