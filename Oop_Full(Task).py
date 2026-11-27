
#1.student
class Student():
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def disply(self):
        print(f"Name is: {self.name} and Roll number is: {self.roll_no} and marks is: {self.marks}")

s1 = Student("Akanksha",16,80)
s2 = Student("Neha",17,89)
s3 = Student("Maya",18,79)
s1.disply()
s2.disply()
s3.disply()

# #2.Bankaccount
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.__balance)

b = BankAccount("Akanksha", 5000)
b.deposit(1000)
b.withdraw(2000)
b.display()

# #3.Employee
class Employee():
    def __init__(self, name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_employee(self):
        print("Name:", self.name)
        print("ID:", self.employee_id)
        print("Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)
        self.department = "IT"

    def display_manager(self):
        self.display_employee()
        print("Department:", self.department)

m = Manager("Maya", 101, 30000)
m.display_manager()

 #4.payment
class CreaditCard():
    def payment(self,amount):
        self.amount = amount
        print("creadited payment",amount)
class UPI():
    def payment(self,amount):
        self.amount = amount
        print("Upi payment:",amount)
class NetBanking():
    def payment(self,amount):
        self.amount = amount
        print("NetBanking :",amount)

def Pay_method(display):
    display.payment(500)

Pay_method(CreaditCard())
Pay_method(UPI())
Pay_method(NetBanking())

#5.
class Vehicle:
    def start(self):
        print("Vehicle is start")

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a start button")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with a driver")
c = Car()
b = Bike()
bu = Bus()
c.start()
b.start()
bu.start()

#6.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def calculate_area(self):
        print("Rectangle Area:", 10 * 5)

class Circle(Shape):
    def calculate_area(self):
        print("Circle Area:", 3.14 * 7 * 7)

r = Rectangle()
c = Circle()
r.calculate_area()
c.calculate_area()

#7.
class Book:
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price

    def display_book(self):
        print(self.book_name, self.author, self.price)

    def apply_discount(self, discount):
        self.price = self.price - discount
        print("Final Price:", self.price)

b1 = Book("Python", "John", 500)
b2 = Book("Java", "James", 600)
b3 = Book("C++", "Robert", 400)

b1.display_book()
b1.apply_discount(50)
b2.display_book()
b2.apply_discount(100)
b3.display_book()
b3.apply_discount(40)

#8.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

class Surgeon(Doctor):
    def __init__(self, name, age, specialization, experience):
        super().__init__(name, age, specialization)
        self.experience = experience

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Experience:", self.experience)

s = Surgeon("Akshu", 23, "Heart", 4)
s.display()

#9.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.get_salary())
        print("Language:", self.language)

d = Developer("Akanksha", 30000, "Python")
d.display()
d.set_salary(40000)
print("Updated Salary:", d.get_salary())

#10.
from abc import ABC, abstractmethod
class FoodOrder(ABC):
    def __init__(self, quantity, price):
        self.__quantity = quantity
        self.price = price

    @abstractmethod
    def calculate_bill(self):
        pass

    def get_quantity(self):
        return self.__quantity

class PizzaOrder(FoodOrder):
    def calculate_bill(self):
        bill = self.get_quantity() * self.price
        print("Pizza Bill:", bill)

class BurgerOrder(FoodOrder):
    def calculate_bill(self):
        bill = self.get_quantity() * self.price
        print("Burger Bill:", bill)

p = PizzaOrder(2, 200)
b = BurgerOrder(3, 100)

# Display bills
p.calculate_bill()
b.calculate_bill()
