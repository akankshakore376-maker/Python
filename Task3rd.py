
name = input("Enter your name: ")
age = int(input("Enter your age: "))
college = input("Enter your college name: ")
course = input("Enter your course: ")

print("Name:", name)
print("Age:", age)
print("College:", college)
print("Course:", course)


#Employee
employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
department = input("Enter department: ")
salary = input("Enter salary: ")

print("\n--- Employee Details ---")
print("Employee Name:", employee_name)
print("Employee ID:", employee_id)
print("Department:", department)
print("Salary:", salary)


#personal
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter your city: ")
profession = input("Enter your profession: ")

print("My name is", first_name, last_name)
print("I live in", city)
print("I am a", profession)


#Two number
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

print("\nFirst Number =", first_number)
print("Second Number =", second_number)


#basic addition
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

addition = first_number + second_number
print("\nAddition =", addition)


#students marks
subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))

total = subject1 + subject2 + subject3
average = total / 3
print("Total Marks =", total)
print("Average Marks =", average)


#Reactangle calculation
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)
print("Area =", area)
print("Perimeter =", perimeter)



#salary
basic_salary = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))

total_salary = basic_salary + hra + da
print("\n--- Salary Details ---")
print("Basic Salary =", basic_salary)
print("HRA =", hra)
print("DA =", da)
print("Total Salary =", total_salary)



#shopping
product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total_amount = price * quantity

print("Product:", product)
print("Price:", price)
print("Quantity:", quantity)
print("Total Amount =", total_amount)



#Tempreture
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("\n--- Temperature Conversion ---")
print("Celsius =", celsius)
print("Fahrenheit =", fahrenheit)