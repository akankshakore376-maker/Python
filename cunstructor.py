#1. student
# class student():
#     def __init__(self,name,roll_number,age):
#         self.name = name
#         self.R_number = roll_number
#         self.Age = age

#     def display(self):
#         print("name :",self.name)
#         print("R_number :",self.R_number)
#         print("Age :",self.Age)

# s1=student("Akshu",16,23)
# s1.display()

#2.Mobile
class Mobile():
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:",self.brand)
        print("model:",self.model)
        print("price:",self.price)

m1 = Mobile("OPPO","A23",26000)
m2 = Mobile("Iphone","17Pro",60000)
m1.display()
m2.display()

#3. car
class Car():
    def __init__(self,brand,color,speed):
        self.brand = brand
        self.color = color
        self.speed = speed
    def display(self):
        print("Brand:", self.brand)
        print("Color:", self.color)
        print("Speed:",self.speed)
c = Car("Thar","Black",60)
c1 = Car("Mahindra","white",50)
c2= Car("Audi","Bule",45)
c.display()
c1.display()
c2.display()

#4. Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r1 = Rectangle(10, 5)
print("Area:", r1.area())

#5. circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
c1 = Circle(5)
print("Area:", c1.area())

#6.Employee
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

e1 = Employee("Akshu", 116, 25000)
print("Name:", e1.name)
print("Employee ID:", e1.emp_id)
print("Annual Salary:", e1.annual_salary())

#7.Bank_Account
class BankAccount:
    def __init__(self, holder, acc_no, balance):
        self.holder = holder
        self.acc_no = acc_no
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
        print("Balance:", self.balance)
b1 = BankAccount("Anu", 12345, 5000)
b1.deposit(2000)
b1.withdraw(1000)
b1.display()

#8.Product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_bill(self):
        return self.price * self.quantity
    
p1 = Product("Laptop", 50000, 2)
print("Product:", p1.name)
print("Total Bill:", p1.total_bill())

#9. student
class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate(self):
        total = self.m1 + self.m2 + self.m3
        percentage = total / 3

        print("Total:", total)
        print("Percentage:", percentage)

        if self.m1 >= 35 and self.m2 >= 35 and self.m3 >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")
s1 = Student(80, 70, 90)
s1.calculate()

#10.Laptop
class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Processor:", self.processor)
        print("Price:", self.price)

L = Laptop("HP", "8GB", "I5", 55000)
L.display()

#11. Book
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def discount(self):
        self.price = self.price - (self.price * 10 / 100)
        print("Discounted Price:", self.price)

b1 = Book("Python", "Akanksha", 500)
b1.discount()

#12. Movie
class Movie:
    def __init__(self, name, ticket_price, tickets):
        self.name = name
        self.ticket_price = ticket_price
        self.tickets = tickets

    def total_cost(self):
        return self.ticket_price * self.tickets

m1 = Movie("Maya", 200, 5)
print("Movie:", m1.name)
print("Total Cost:", m1.total_cost())

#13. shopping cart
class ShoppingCart:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def calculate_bill(self):
        bill = self.price * self.quantity

        if bill > 5000:
            bill = bill - (bill * 5 / 100)
        print("Final Bill:", bill)

s1 = ShoppingCart(2000, 3)
s1.calculate_bill()

#14. Temperature
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def convert(self):
        fahrenheit = (self.celsius * 9/5) + 32
        print("Fahrenheit:", fahrenheit)
t1 = Temperature(30)
t1.convert()

#15.Electricity bill
class ElectricityBill:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def calculate_bill(self):
        rate = 7
        bill = self.units * rate

        print("Customer Name:", self.name)
        print("Units:", self.units)
        print("Total Bill:", bill)

e1 = ElectricityBill("Abhi", 100)
e1.calculate_bill()

#16. class Student:
class Student:
    def __init__(self, name="Raam", age=18):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
s1 = Student()
s1.display()

#17. Employee
class Employee:
    def __init__(self, department="IT", salary=25000):
        self.department = department
        self.salary = salary

    def display(self):
        print("Department:", self.department)
        print("Salary:", self.salary)

e1 = Employee()
e1.display()

#18.Mobile
class Mobile:
    def __init__(self, brand="Samsung", price=15000):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)
m1 = Mobile()
m1.display()

#19. car
class Car:
    def __init__(self, colour="White", speed=0):
        self.colour = colour
        self.speed = speed

    def display(self):
        print("Colour:", self.colour)
        print("Speed:", self.speed)
c1 = Car()
c1.display()

#20. BankAccount
class BankAccount:
    def __init__(self, balance=1000):
        self.balance = balance

    def display(self):
        print("Balance:", self.balance)
b1 = BankAccount()
b1.display()

