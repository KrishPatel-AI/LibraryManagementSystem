#library.py

import os
import json
from allclasses import Transaction

class Library:
    def __init__(self):
        self.file_name ="data.json"

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
        self.data["books"].append(book.to_dict())
        self.save_data()
        print("Book Added")





    def register_member(self, member):
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
                print(book)

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
            print(transaction)
