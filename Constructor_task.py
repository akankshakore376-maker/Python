#1
class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)

s1 = Student("Akshu", 101, "Python")
s1.display_details()

#2
class Employee():
    def __init__(self,e_name,e_id,salary):
        self.e_name = e_name
        self.e_id = e_id
        self.salary = salary

    def calculate(self):
        self.A_salary = self.salary * 12

    def display(self):
        print("E_name:", self.e_name)
        print("E_id:", self.e_id)
        print("Salary:", self.salary)
        print("Annual salary:", self.A_salary)

E1 = Employee("yash",109,5000)
E1.calculate()
E1.display()

#3
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def discount(self, discount):
        final_price = self.price - discount
        print("Final Price:", final_price)

    def display(self):
            print("Brand:", self.brand)
            print("Model:", self.model)
            print("Price:", self.price)

m1 = Mobile("Samsung", "S24", 50000)
m1.discount(500)
m1.display()

#4
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
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

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

b1 = BankAccount("Akanksha", 10000)
b1.deposit(5000)
b1.withdraw(2000)
b1.display_balance()

#5
class Car:
    def __init__(self, car_name, rent_per_day):
        self.car_name = car_name
        self.rent_per_day = rent_per_day

    def calculate_rent(self, days):
        total_rent = self.rent_per_day * days
        print("Car Name:", self.car_name)
        print("Rental Days:", days)
        print("Total Rent:", total_rent)
c1 = Car("BMW", 3000)
c1.calculate_rent(5)
          
#6.
class Laptop:
    def __init__(self):
        self.brand = "Dell"
        self.ram = "16GB"
        self.price = 55000

    def display_details(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Price:", self.price)
L = Laptop()
L.display_details()

 #7.
class Book:
    def __init__(self, book_name, author_name, price):
        self.book_name = book_name
        self.author_name = author_name
        self.price = price

    def display(self):
        print("Book Name:", self.book_name)
        print("Author:", self.author_name)
        print("Price:", self.price)
b1 = Book("Python Programming", "Akshu", 500)
b2 = Book("Java Programming", "Sanu", 600)
b1.display()
b2.display()         

#8.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate(self):
        area = self.length * self.width
        print("Area of Rectangle:", area)
r1 = Rectangle(10, 5)
r1.calculate()

#9.
class ElectricityBill:
    def __init__(self, customer_name, units):
        self.customer_name = customer_name
        self.units = units

    def calculate(self):
        if self.units <= 100:
            bill = self.units * 5

        elif self.units <= 200:
            bill = (100 * 5) + ((self.units - 100) * 7)

        else:
            bill = (100 * 5) + (100 * 7) + ((self.units - 200) * 10)

        print("Customer Name:", self.customer_name)
        print("Units Consumed:", self.units)
        print("Total Bill: ", bill)
e1 = ElectricityBill("Akanksha", 250)
e1.calculate()

#10.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def calculate(self):
        total = self.price * self.quantity
        print("Total Price:", total)

    def update(self, new_quantity):
        self.quantity = new_quantity
        print("Updated Quantity:", self.quantity)
p1 = Product("Laptop", 50000, 2)
p1.display()
p1.calculate()
p1.update(5)
p1.calculate()

#11.
class Employee:
    company_name = "TCS"
    employee_count = 0

    def __init__(self, name, emp_id):
        self.employee_name = name
        self.employee_id = emp_id
        Employee.employee_count += 1

    def display(self):
        print("Company:", Employee.company_name)
        print("Employee Name:", self.employee_name)
        print("Employee ID:", self.employee_id)
        print("Total Employees:", Employee.employee_count)
e1 = Employee("Akshu", 101)
e2 = Employee("Priya", 102)
e1.display()
e2.display()

#12.
class Student:
    school_name = "ABC School"

    def __init__(self, name, roll_no):
        self.student_name = name
        self.roll_number = roll_no

    def display(self):
        percentage = 85
        print("School Name:", Student.school_name)
        print("Student Name:", self.student_name)
        print("Roll Number:", self.roll_number)
        print("Percentage:", percentage)
s1 = Student("Neha", 101)
s1.display()

#13.
class ShoppingCart:
    discount_percentage = 10

    def __init__(self, customer_name, total_amount):
        self.customer_name = customer_name
        self.total_amount = total_amount

    def calculate(self):
        discount = self.total_amount * ShoppingCart.discount_percentage / 100
        final_amount = self.total_amount - discount
        print("Customer:", self.customer_name)
        print("Total Amount:", self.total_amount)
        print("Discount:", discount)
        print("Final Payable Amount:", final_amount)
c1 = ShoppingCart("Akash", 5000)
c1.calculate()

#14.
class Patient:
    hospital_name = "City Hospital"

    def __init__(self, name, age, disease):
        self.patient_name = name
        self.patient_age = age
        self.disease = disease

    def display(self):
        print("Hospital:", Patient.hospital_name)
        print("Patient Name:", self.patient_name)
        print("Age:", self.patient_age)
        print("Disease:", self.disease)

p1 = Patient("Akanksha", 23, "Fever")
p2 = Patient("Neha", 30, "Cold")
p1.display()
p2.display()

#15.
class Course:
    institute_name = "Kiran Academy Institute"

    def __init__(self, course_name, course_fee):
        self.course_name = course_name
        self.course_fee = course_fee

    def calculate(self):
        discount = 10
        final_fee = self.course_fee - (self.course_fee * discount / 100)
        print("Institute:", Course.institute_name)
        print("Course Name:", self.course_name)
        print("Original Fee:", self.course_fee)
        print("Discount:", discount, "%")
        print("Final Fee:", final_fee)
c1 = Course("Python", 10000)
c1.calculate()

#16.
class ATM:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient Balance")
            return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

a1 = ATM("Akshu", 10000)
a1.check_balance()
new_balance = a1.withdraw(2000)
print("Balance After Withdrawal:", new_balance)
new_balance = a1.deposit(5000)
print("Balance After Deposit:", new_balance)

#17.
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_to_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    
t1 = Temperature(37)
print("Celsius to Fahrenheit:", t1.celsius_to_fahrenheit())
print("Fahrenheit to Celsius:", t1.fahrenheit_to_celsius(98.6))

#18.
class StudentResult:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate_total(self):
        total = self.m1 + self.m2 + self.m3
        return total

    def calculate_percentage(self):
        percentage = (self.calculate_total() / 300) * 100
        return percentage

    def display(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.calculate_total())
        print("Percentage:", self.calculate_percentage())
s1 = StudentResult("Akshu", 80, 85, 90)
s1.display()

#19.
class FoodOrder:
    def __init__(self, customer, food_item, price, quantity):
        self.customer = customer
        self.food_item = food_item
        self.price = price
        self.quantity = quantity

    def calculate(self):
        total = self.price * self.quantity
        return total

    def apply_coupon(self, discount):
        total = self.calculate()
        final_bill = total - discount
        return final_bill

    def display(self):
        print("Customer Name:", self.customer)
        print("Food Item:", self.food_item)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Bill:", self.calculate())
        print("Final Bill:", self.apply_coupon(50))

f1 = FoodOrder("Nisha", "Pizza", 200, 3)
f1.display()

#20.
class Vehicle:
    vehicle_count = 0

    def __init__(self, name, vehicle_type, price):
        self.vehicle_name = name
        self.vehicle_type = vehicle_type
        self.vehicle_price = price

        Vehicle.vehicle_count += 1

    def display(self):
        print("Vehicle Name:", self.vehicle_name)
        print("Vehicle Type:", self.vehicle_type)
        print("Vehicle Price:", self.vehicle_price)
        print("Total Vehicles:", Vehicle.vehicle_count)

    def calculate_insurance(self, rate):
        insurance = self.vehicle_price * rate / 100
        print("Insurance Amount:", insurance)

    def update_price(self, new_price):
        self.vehicle_price = new_price
        print("Updated Price:", self.vehicle_price)

v1 = Vehicle("Activa", "Scooter", 80000)
v2 = Vehicle("Royal Enfield", "Bike", 200000)
v1.display()
v1.calculate_insurance(5)
v1.update_price(1100000)
v2.display()
print("Total Vehicles Created:", Vehicle.vehicle_count)