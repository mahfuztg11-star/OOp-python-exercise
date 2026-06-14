class Student:
    def __init__(self, name):
        self.name = name
        print(f"Student {self.name} has been created.")

    def __del__(self):
        print(f"Student {self.name} has been deleted.")


student1 = Student("Mahfuz")
student2 = Student("Rahim")
student3 = Student("Karim")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Car {self.brand} {self.model} created.")

    def __del__(self):
        print(f"Car {self.brand} {self.model} destroyed.")


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"Book '{self.title}' added.")

    def __del__(self):
        print(f"Book '{self.title}' removed.")


book1 = Book("Basics", "John Doe")
book2 = Book("Learning", "Andrew Ng")

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print(f"Account {self.account_number} created with balance {self.balance}.")

    def __del__(self):
        print(f"Account {self.account_number} destroyed.")


account1 = Account("ACC101", 5000)
account2 = Account("ACC102", 12000)

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        print(f"Mobile {self.brand} created. Price: {self.price}")

    def __del__(self):
        print(f"Mobile {self.brand} destroyed.")


mobile1 = Mobile("Samsung", 25000)
mobile2 = Mobile("Xiaomi", 20000)
mobile3 = Mobile("iPhone", 90000)