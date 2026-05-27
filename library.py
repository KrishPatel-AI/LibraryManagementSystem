#library.py

import os
import json
from allclasses import Transaction

class Library:
    def __init__(self):
        self.file_name = os.path.join(os.path.dirname(__file__), "data.json")

        if not os.path.exists(self.file_name):
            self.data = {
                "books":[],
                "members":[],
                "transactions":[]
            }
            self.save_data()
        else:
            self.load_data()



    def load_data(self):
        try:
            with open(self.file_name, "r") as file:
                self.data = json.load(file)

        except json.JSONDecodeError:
            self.data = {
                "books": [],
                "members": [],
                "transactions": []
            }
            self.save_data()




    def save_data(self):
        with open(self.file_name, "w") as file:
            json.dump(self.data, file, indent=4)





    def add_book(self, book):
        for book_existed in self.data["books"]:
            if book_existed["isbn"] == book.isbn:
                print("Book ISBN already exists")
                return

        self.data["books"].append(book.to_dict())
        self.save_data()
        print("Book Added")





    def register_member(self, member):
        for member_existed in self.data["members"]:
            if member_existed["memberID"] == member.memberID:
                print("Member ID already Existed")
                return

        self.data["members"].append(member.to_dict())
        self.save_data()
        print("Member Registered")






    def show_books(self):
        if len(self.data["books"]) == 0:
            print("No books Available")
            return

        for book in self.data["books"]:
            print("Title: " + book["title"])
            print("Author: " + book["author"])
            print("ISBN: " + book["isbn"])
            print("Category: " + book["category"])
            print("Quantity:", book["quantity"])






    def search_book(self, keyword):
        found = False

        for book in self.data["books"]:
            if (

                keyword.lower() in book["title"].lower()
                or keyword.lower() in book["author"].lower()
                or keyword.lower() in book["category"].lower()
            ):
                found = True
                print("\nFound Book")
                print("Title:" + book["title"])
                print("Author:" + book["author"])
                print("ISBN:" + book["isbn"])
                print("Category:" + book["category"])
                print("Quantity:" , book["quantity"])

        if not found:
            print("No matching books found")






    def issue_book(self, memberID, isbn):
        member_exists = False
        for member in self.data["members"]:
            if member["memberID"] == memberID:
                member_exists = True
                break

        if not member_exists:
                print("Member not found.")
                return

        for book in self.data["books"]:
             if book["isbn"] == isbn:
                if book["quantity"] <= 0:
                    print("Book is out of Stock")
                    return
                book["quantity"] -= 1

                transaction = Transaction(memberID, isbn, "issue")
                self.data["transactions"].append(transaction.to_dict())

                self.save_data()

                print("Book issued successfully")
                return

        print("Book not found.")






    def return_book(self, memberID, isbn ):
        member_exists = False
        for member in self.data["members"]:
            if member["memberID"] == memberID:
                member_exists = True
                break
        if not member_exists:
            print("Member not found.")
            return

        issue_count = 0
        return_count = 0

        for transaction in self.data["transactions"]:
            if (
                transaction["memberID"] == memberID
                and transaction["isbn"] == isbn
            ):
                if transaction["action"] == "issue":
                    issue_count += 1

                elif transaction["action"] == "return":
                    return_count += 1
        if issue_count <= return_count:
            print("Member did not issue this book.")
            return


        for book in self.data["books"]:

            if book["isbn"] == isbn:
                book["quantity"] += 1
                transaction = Transaction(memberID, isbn, "return")
                self.data["transactions"].append(transaction.to_dict())
                self.save_data()
                print("Book returned successfully")
                return

        print("Book not found.")








    def show_transactions(self):

        if len(self.data["transactions"]) == 0:
            print("No transactions history")
            return

        for transaction in self.data["transactions"]:
            print("Member ID:", transaction["memberID"])
            print("ISBN:", transaction["isbn"])
            print("Action", transaction["action"])

            print()
