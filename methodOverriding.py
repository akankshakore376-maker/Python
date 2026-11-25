#MethodOverriding
#1.
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
obj = Dog()
obj.sound()

#2.
class Mobile:
    def camera(self):
        print("Normal camera")

class Samsung(Mobile):
    def camera(self):
        print("Samsung camera")
obj = Samsung()
obj.camera()

#3.
class Bank:
    def rate(self):
        print("Interest rate is 4%")

class SBI(Bank):
    def rate(self):
        print("Interest rate is 6%")
obj = SBI()
obj.rate()

#4.
class Car:
    def start(self):
        print("Car starts")

class BMW(Car):
    def start(self):
        print("BMW starts with a button")
obj = BMW()
obj.start()

#5.
class Student:
    def study(self):
        print("Student studies for 2 hours")

class Akanksha(Student):
    def study(self):
        print("Akanksha studies for 4 hours")
obj = Akanksha()
obj.study()

#6.
class Shop:
    def price(self):
        print("Price is 100")

class Medical(Shop):
    def price(self):
        print("Price is 50")
obj = Medical()
obj.price()

#7.
class Teacher:
    def teach(self):
        print("Teaching English")

class Maths(Teacher):
    def teach(self):
        print("Teaching Maths")
obj = Maths()
obj.teach()

#8.
class Laptop:
    def work(self):
        print("Laptop is working")

class Dell(Laptop):
    def work(self):
        print("Dell laptop is working")
obj = Dell()
obj.work()

#9.
class Food:
    def taste(self):
        print("Food is tasty")

class Pizza(Food):
    def taste(self):
        print("Pizza is very tasty")
obj = Pizza()
obj.taste()

#10.
class Hospital:
    def fees(self):
        print("Normal fees is 500")

class City(Hospital):
    def fees(self):
        print("Normal fees is 1000")
obj = City()
obj.fees()

#11.
class TV:
    def show(self):
        print("Showing normal channels")

class SmartTV(TV):
    def show(self):
        print("Showing online channels")
obj = SmartTV()
obj.show()

#12.
class IceCream:
    def flavour(self):
        print("Vanilla flavour")

class Chocolate(IceCream):
    def flavour(self):
        print("Chocolate flavour")
obj = Chocolate()
obj.flavour()

#13.
class Delivery:
    def order(self):
        print("Order will arrive tomorrow")

class Amazon(Delivery):
    def order(self):
        print("Order will arrive today")
obj = Amazon()
obj.order()

#14.
class Game:
    def play(self):
        print("Playing a game")

class Cricket(Game):
    def play(self):
        print("Playing cricket")
obj = Cricket()
obj.play()

#15.
class Camera:
    def photo(self):
        print("Taking a normal photo")

class Phone(Camera):
    def photo(self):
        print("Taking a selfie")
obj = Phone()
obj.photo()

#16.
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bus(Vehicle):
    def move(self):
        print("Bus is carrying students")
obj = Bus()
obj.move()

#17.
class Person:
    def work(self):
        print("Person is working")

class Police(Person):
    def work(self):
        print("Police are controlling traffic")

obj = Police()
obj.work()

#18.
class Doctor:
    def check(self):
        print("Checking the patient")

class Dentist(Doctor):
    def check(self):
        print("Checking the patient's teeth")
obj = Dentist()
obj.check()

#19.
class Fruit:
    def taste(self):
        print("Fruit tastes sweet")

class Lemon(Fruit):
    def taste(self):
        print("Lemon tastes sour")
obj = Lemon()
obj.taste()

#20.
class Computer:
    def display(self):
        print("Showing information")

class Laptop(Computer):
    def display(self):
        print("Showing information on laptop screen")
obj = Laptop()
obj.display()

#MethodOverloading
#1.
class Calculator:
    def add(self, a, b=0, c=0):
        print("Sum:", a + b + c)

obj = Calculator()
obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)

#2.
class Calculator:

    def multiply(self, *args):
        result = 1

        for i in args:
            result = result * i

        print("Multiplication:", result)
c = Calculator()
c.multiply(5, 2)
c.multiply(5, 2, 3)


