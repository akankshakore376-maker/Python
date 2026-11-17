# a=10
# b=10.5
# c="hii"
# d=True
# e=5+3j
# f=[1,2,3,4]
# g=(5,6,7)
# h={10,20,30}
# i={"name" : "ananya","age":7}
# j=None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))
# print(type(i))
# print(type(j))

# x=100
# print(type(x))
# x="python"
# print(type(x))

# emp_id = 101
# name = "Rahul"
# salary = 35000.50
# department = "IT"
# status = True
# print(emp_id)
# print(name)
# print(salary)
# print(department)
# print(status)

# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
# area = length * width
# print("Area of rectangle:", area)

# a=10
# b=20
# a,b=b,a
# print("a=",a)
# print("b=",b)

# a = 10
# b = 20.5
# c = "30"
# print(type(a + b))
# print(type(str(a)))
# print(type(float(c)))

# a="20" 
# b=int(a)
# print("square:",b*b)

# a = 45
# print(float(a))
# print(str(a))
# print(bool(a))

# a=99.99
# b=int(a)
# print(b)

# num = input("Enter a number: ")
# num = int(num)
# print("Number:", num)
# print("Data type:", type(num))

# m1 = input("Enter marks in subject 1: ")
# m2 = input("Enter marks in subject 2: ")
# m3 = input("Enter marks in subject 3: ")
# total = int(m1) + int(m2) + int(m3)
# percentage = (total / 300) * 100
# print("Total marks:", total)
# print("Percentage:", percentage)

# a = 100
# b = 20.5
# print(str(a) + str(b))
# print(int(b))
# print(float(a))
# print(bool(0))
# print(bool(""))

# name = input("Enter your full name: ")
# print("Uppercase:", name.upper())
# print("Lowercase:", name.lower())

# text = input("Enter a string: ")
# print("Number of characters:", len(text))

# text = input("Enter a string: ")
# reverse = ""
# for ch in text:
#     reverse = ch + reverse
# print("Reversed string:", reverse)

# text = input("Enter a string: ")
# count = text.lower().count("a")
# print("Number of a:", count)

# text = input("Enter a sentence: ")
# result = text.replace(" ", "-")
# print(result)

# sentence = input("Enter a sentence: ")
# word = input("Enter a word: ")
# if word in sentence.split():
#     print("Word exists")
# else:
#     print("Word does not exist")

# email = input("Enter email address: ")
# username = email.split("@")[0]
# domain = email.split("@")[1]
# print("Username:", username)
# print("Domain:", domain)

# name = "Rahul"
# age = 20
# city = "Pune"
# print(f"My name is {name}. I am {age} years old and I live in {city}.")

# numbers = [10, 20, 55, 60, 75, 30, 90, 45, 80, 15, 65, 25, 100, 40, 50]
# for num in numbers:
#     if num > 50:
#         print(num)

# num=[10,20,30,40,50]
# unique=list(set(num))
# unique.sort()
# print("second largest:",unique[-2])

# num=[1,2,3,4,2,4,5,6,4]
# result=list(set(num))
# print(result)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = list1 + list2
# print(list3)

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common = []
# for x in list1:
#     if x in list2 and x not in common:
#         common.append(x)
# print(common)

# marks = [35, 45, 60, 25, 80, 39, 90]
# count = 0
# for mark in marks:
#     if mark >= 40:
#         count += 1
# print("Number of students passed:", count)

# numbers = [10, -5, 0, 20, -10, 30, 0]
# positive = []
# negative = []
# zero = []
# for num in numbers:
#     if num > 0:
#         positive.append(num)
#     elif num < 0:
#         negative.append(num)
#     else:
#         zero.append(num)
# print("Positive:", positive)
# print("Negative:", negative)
# print("Zero:", zero)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# total = 0
# for num in numbers:
#     if num % 2 == 0:
#         total += num
# print("Sum of even numbers:", total)

# students = [["Rahul", 85],["Priya", 90], ["Amit", 75]]
# print(students[0])
# print(students[0][0])
# print(students[0][1])
# print(students[1][0])
# print(students[1][1])

# numbers = [1, 2, 3, 4, 5]
# reverse = []
# for num in numbers:
#     reverse.insert(0, num)
# print(reverse)

# numbers = (10, 20, 55, 60, 75, 30, 90, 45, 80, 15, 65, 25, 100, 40, 50)
# for num in numbers:
#     if num > 50:
#         print(num)

# numbers = (10, 50, 30, 80, 60)
# unique = sorted(set(numbers))
# print("Second largest:", unique[-2])

# numbers = (1, 2, 3, 2, 4, 1, 5)
# result = tuple(set(numbers))
# print(result)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)