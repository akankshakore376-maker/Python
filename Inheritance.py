#1. Single Inheritence
class Father():
    def house(self):
        print("Father has a house")

class Daughter(Father):
    def scotty(self):
        print("Daughter has a scotty")
s = Daughter()
s.house()
s.scotty()

#2.
class Student():
    def name(self):
        print("Name: Akanksha")

class Marks(Student):
    def show(self):
        print("Marks: 85")
m = Marks()
m.name()
m.show()

#3.
class Employee:
    def emp(self):
        print("Employee name: Nisha")

class Salary(Employee):
    def sal(self):
        print("Salary: 20000")
s = Salary()
s.emp()
s.sal()

#4.
class Animal:
    def eat(self):
        print("Animal eating food")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")
d = Dog()
d.eat()
d.bark()

#5.
class A():
    def add(self):
        a = 10
        b = 20
        print("Addition:", a + b)

class B(A):
    def display(self):
        print("child class")
obj = B()
obj.add()
obj.display()

#6. Multiple Inheritance
class Father:
    def display(self):
        print("This is father class")

class Mother:
    def show(self):
        print("This is mother class")

class Son(Father, Mother):
    def show2(self):
        print("This is son class")
s = Son()
s.display()
s.show()
s.show2()

#7.
class Maths:
    def maths(self):
        print("Maths marks: 80")

class Science:
    def science(self):
        print("Science marks: 90")

class Student(Maths, Science):
    def student(self):
        print("Student Name:  Akanksha")

s = Student()
s.student()
s.maths()
s.science()

#8.
class A:
    def display(self):
        print("Welcome to Python")

class B:
    def show(self):
        print("Python is easy")

class C(A, B):
    def subject(self):
        print("Python")
obj = C()
obj.display()
obj.show()
obj.subject()

#9.
class Car:
    def car(self):
        print("This is a car")

class Bike:
    def bike(self):
        print("This is a bike")

class Vehicle(Car, Bike):
    def show(self):
        print("This is a vehicle")

v = Vehicle()
v.car()
v.bike()
v.show()

#10.
class Father:
    def money(self):
        print("Father gives money")

class Mother:
    def love(self):
        print("Mother gives love")

class Child(Father, Mother):
    def study(self):
        print("Child is studying")

c = Child()
c.money()
c.love()
c.study()

#11. Multilevel Inheritance
class A:
    def show(self):
        print("Class A")

class B(A):
    def show2(self):
        print("Class B")

class C(B):
    def display(self):
        print("Class C")
obj = C()
obj.show()
obj.show2()
obj.display()

#12.
class Student:
    def name(self):
        print("Student name: Akanksha")

class Marks(Student):
    def marks(self):
        print("Marks: 80")

class Result(Marks):
    def result(self):
        print("Result: Pass")

r = Result()
r.name()
r.marks()
r.result()

#13.
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Dog):
    def play(self):
        print("cat id playing")
p = Cat()
p.eat()
p.bark()
p.play()

#14.
class Employee:
    def name(self):
        print("Employee: Anil")

class Manager(Employee):
    def work(self):
        print("Manager manages work")

class Boss(Manager):
    def office(self):
        print("Boss is in office")
b = Boss()
b.name()
b.work()
b.office()

#15.
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Scotty(Car):
    def speed(self):
        print("Scotty is slow")
s = Scotty()
s.start()
s.drive()
s.speed()

#16. Hierarchical Inheritance
class Father():
    def show(self):
        print("father class")

class Son(Father):
    def son(self):
        print("son class")

class Daughter(Father):
    def daughter(self):
        print("Daughter class")
s = Son()
d = Daughter()
s.show()
s.son()
d.show()
d.daughter()

#17.
class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.eat()
d.bark()
c.eat()
c.sound()

#18.
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def show(self):
        print("This is car")

class Bike(Vehicle):
    def display(self):
        print("This is bike")
c = Car()
b = Bike()
c.start()
c.show()
b.start()
b.display()

#19. Hybrid Inheritance
class A:
    def show1(self):
        print("Class A")

class B(A):
    def show2(self):
        print("Class B")

class C(A):
    def show3(self):
        print("Class C")

class D(B, C):
    def dispaly(self):
        print("Class D")
obj = D()
obj.show1()
obj.show2()
obj.show3()
obj.dispaly()

#20.
class Student:
    def student(self):
        print("Student details")

class Sports(Student):
    def sports(self):
        print("Sports marks: 80")

class Exam(Student):
    def exam(self):
        print("Exam marks: 90")

class Result(Sports, Exam):
    def result(self):
        print("Student passed")
r = Result()
r.student()
r.sports()
r.exam()
r.result()