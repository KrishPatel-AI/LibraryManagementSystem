import datetime

class Book:
    def __init__(self, title, author, isbn, category, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.quantity = quantity

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "category": self.category,
            "quantity": self.quantity
        }

class Member:
    def __init__(self, name, email, memberID):
        self.name = name
        self.email = email
        self.memberID = memberID

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "memberID": self.memberID,
            "type": "normal"
        }

class PremiumMember(Member):
    def __init__(self, name, email, memberID):
        super().__init__(name, email, memberID)


    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "memberID": self.memberID,
            "type": "premium",

        }

class Transaction:
    def __init__(self, memberID, isbn, action):
        self.memberID = memberID
        self.isbn = isbn
        self.action = action
        self.date = datetime.datetime.now().isoformat()

    def to_dict(self):
        return {
            "memberID": self.memberID,
            "isbn": self.isbn,
            "action": self.action,
            "date": self.date
        }