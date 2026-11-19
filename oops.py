#1. Person Class
class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
p = Person()
p.set_details("Akshu", 23)
p.display()

#2. Student Class
class Student:
    def set_details(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Course:", self.course)
s = Student()
s.set_details("Abhi", 116, "BSC")
s.display()

#3. Calculator Class
class Calculator:
    def set_numbers(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print("Addition:", self.a + self.b)

    def subtraction(self):
        print("Subtraction:", self.a - self.b)

    def multiplication(self):
        print("Multiplication:", self.a * self.b)

    def division(self):
        if self.b != 0:
            print("Division:", self.a / self.b)
        else:
            print("Cannot divide by zero")
c = Calculator()
c.set_numbers(20, 10)
c.addition()
c.subtraction()
c.multiplication()
c.division()

#4. Square Class
class Square:
    def set_side(self, side):
        self.side = side

    def area(self):
        print("Area:", self.side * self.side)

    def perimeter(self):
        print("Perimeter:", 4 * self.side)
s = Square()
s.set_side(5)
s.area()
s.perimeter()

#5. Rectangle Class
class Rectangle:
    def set_values(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area:", self.length * self.breadth)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.breadth))
r = Rectangle()
r.set_values(10, 5)
r.area()
r.perimeter()

#6. Employee Class
class Employee:
    def set_details(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Annual Salary:", self.salary * 12)
e = Employee()
e.set_details("Akanksha", 25000)
e.display()

#7. Number Class
class Number:
    def check(self, num):
        if num > 0:
            print("Positive Number")
        elif num < 0:
            print("Negative Number")
        else:
            print("Zero")
n = Number()
n.check(-5)

#8. EvenOdd Class
class EvenOdd:
    def check(self, num):
        if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")
e = EvenOdd()
e.check(7)

#9. Voting Class
class Voting:
    def check_age(self, age):
        if age >= 18:
            print("Eligible for Voting")
        else:
            print("Not Eligible for Voting")
v = Voting()
v.check_age(20)

#10. Product Class
class Product:
    def set_details(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        total = self.price * self.quantity
        print("Product Name:", self.name)
        print("Total Amount:", total)
p = Product()
p.set_details("Pen", 10, 5)
p.display()

#11. Mobile Class
class Mobile:
    def set_details(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
m = Mobile()
m.set_details("Samsung", "S24", 50000)
m.display()

#12. BankAccount Class
class BankAccount:
    def set_details(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def display(self):
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)
b = BankAccount()
b.set_details("Rahul", 5000)
b.deposit(2000)
b.display()

#13. Book Class
class Book:
    def set_details(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
b = Book()
b.set_details("Python Programming", "Guido", 500)
b.display()

#14. Circle Class
class Circle:
    def set_radius(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", 3.14 * self.radius * self.radius)
c = Circle()
c.set_radius(5)
c.area()

#15. Temperature Class
class Temperature:
    def set_celsius(self, c):
        self.celsius = c

    def convert(self):
        f = (self.celsius * 9/5) + 32
        print("Fahrenheit:", f)
t = Temperature()
t.set_celsius(37)
t.convert()

#16. ExamResult Class
class ExamResult:
    def set_details(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)

        if self.marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")
e = ExamResult()
e.set_details("Nisha", 75)
e.display()

#17. Car Class
class Car:
    def set_details(self, brand, colour, speed):
        self.brand = brand
        self.colour = colour
        self.speed = speed

    def display(self):
        print("Brand:", self.brand)
        print("Colour:", self.colour)
        print("Speed:", self.speed)

    def increase_speed(self, amount):
        self.speed += amount
        print("New Speed:", self.speed)
c = Car()
c.set_details("Toyota", "Black", 60)
c.display()
c.increase_speed(20)

#18. Movie Class
class Movie:
    def set_details(self, name, language, rating):
        self.name = name
        self.language = language
        self.rating = rating

    def display(self):
        print("Movie Name:", self.name)
        print("Language:", self.language)
        print("Rating:", self.rating)
m = Movie()
m.set_details("3 Idiots", "Hindi", 9)
m.display()

#19. ATM Class
class ATM:
    def set_balance(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Available Balance:", self.balance)
a = ATM()
a.set_balance(10000)
a.deposit(2000)
a.withdraw(3000)
a.display()

#20. Team Class
class Team:
    def set_details(self, name, jersey):
        self.name = name
        self.jersey = jersey

    def display(self):
        print("Player Name:", self.name)
        print("Jersey Number:", self.jersey)
p1 = Team()
p1.set_details("Akanksha", 9)

p2 = Team()
p2.set_details("Abhi", 7)

p3 = Team()
p3.set_details("Rohan", 18)

print("Player 1 Details:")
p1.display()

print("\nPlayer 2 Details:")
p2.display()

print("\nPlayer 3 Details:")
p3.display()