#student
class Student():
    def __init__(self,name,marks):
      self.__name = name
      self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

s1 = Student("Akanksha",80)    
print(s1.get_marks())
s1.set_marks(95)
print(s1.get_marks())

#2.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Money deposited")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Money withdrawn")
        else:
            print("Invalid amount")

    def check_balance(self):
        print("Balance:", self.__balance)

b = BankAccount(5000)
b.deposit(1000)
b.withdraw(500)
b.check_balance()

#3.
class Employee:
    def __init__(self, id, salary):
        self.__id = id
        self.__salary = salary

    def get_id(self):
        return self.__id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

e = Employee(101, 20000)
print(e.get_id())
print(e.get_salary())
e.set_salary(30000)
print(e.get_salary())

#4
class Mobile:
    def __init__(self, password):
        self.__password = password

    def get_mobile(self, password):
        if self.__password == password:
            print("Correct password")
        else:
            print("Wrong password")

    def set_mobile(self, old, new):
        if self.__password == old:
            self.__password = new
            print("Password changed")
        else:
            print("Wrong old password")

m = Mobile("1234")
m.get_mobile("1234")
m.set_mobile("1234", "5678")
m.get_mobile("5678")

#5
class Car:
    def __init__(self):
        self.__speed = 0

    def accelerate(self):
        if self.__speed < 180:
            self.__speed += 10
        print("Speed:", self.__speed)

    def brake(self):
        if self.__speed > 0:
            self.__speed -= 10
        print("Speed:", self.__speed)

c = Car()
c.accelerate()
c.accelerate()
c.brake()

#6.
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Invalid price")

p = Product("Laptop", 50000)
print(p.price)
p.price = 60000
print(p.price)

#7.
class LibraryBook:
    def __init__(self):
        self.__available = True

    def issue_book(self):
        if self.__available:
            self.__available = False
            print("Book issued")
        else:
            print("Book already issued")

    def return_book(self):
        self.__available = True
        print("Book returned")

b = LibraryBook()
b.issue_book()
b.issue_book()
b.return_book()

#8.
class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Money added")

    def spend_money(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Money spent")
        else:
            print("Not enough money")

    def show_balance(self):
        print("Balance:", self.__balance)

w = Wallet(1000)
w.add_money(500)
w.spend_money(200)
w.show_balance()

#9.
class ElectricityBill:
    def __init__(self, units):
        self.__units = units

    def set_units(self, units):
        if units >= 0:
            self.__units = units
        else:
            print("Invalid units")

    def calculate_bill(self):
        bill = self.__units * 5
        print("Total Bill:", bill)

e = ElectricityBill(100)
e.calculate_bill()
e.set_units(200)
e.calculate_bill()

#10.
class ShoppingCart:
    def __init__(self):
        self.__total = 0
        self.__count = 0

    def add_item(self, price):
        if price > 0:
            self.__total += price
            self.__count += 1

    def remove_item(self, price):
        if price > 0 and self.__count > 0 and price <= self.__total:
            self.__total -= price
            self.__count -= 1

    def display(self):
        print("Total:", self.__total)
        print("Items:", self.__count)

s = ShoppingCart()
s.add_item(100)
s.add_item(200)
s.display()
s.remove_item(100)
s.display()