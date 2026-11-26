#1.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")
d = Dog()
d.sound()

#2.

from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass

class BMW(Car):
    def start(self):
        print("BMW starts")
c = BMW()
c.start()

#3.
from abc import ABC, abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass

class SBI(ATM):
    def withdraw(self):
        print("Money withdrawn")
a = SBI()
a.withdraw()

#4.
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class GooglePay(Payment):
    def pay(self):
        print("Payment using Google Pay")
p = GooglePay()
p.pay()

#5.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area = 100")
s = Square()
s.area()

#6.
from abc import ABC, abstractmethod
class Mobile(ABC):
    @abstractmethod
    def call(self):
        pass

class Samsung(Mobile):
    def call(self):
        print("Calling using Samsung")
m = Samsung()
m.call()

#7.
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        print("Salary is 50000")
e = Manager()
e.salary()

#8.
from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass

class SBI(Bank):
    def interest(self):
        print("Interest rate is 7%")
b = SBI()
b.interest()

#9.
from abc import ABC, abstractmethod
class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class HP(Printer):
    def print_document(self):
        print("Printing document")
p = HP()
p.print_document()

#10.
from abc import ABC, abstractmethod
class Laptop(ABC):
    @abstractmethod
    def os(self):
        pass

class Dell(Laptop):
    def os(self):
        print("Windows operating system")
l = Dell()
l.os()

#11.
from abc import ABC, abstractmethod
class Food(ABC):
    @abstractmethod
    def cook(self):
        pass

class Pizza(Food):
    def cook(self):
        print("Preparing pizza")
f = Pizza()
f.cook()

#12.
from abc import ABC, abstractmethod
class Delivery(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Amazon(Delivery):
    def deliver(self):
        print("Order delivered")
d = Amazon()
d.deliver()

#13.
from abc import ABC, abstractmethod
class School(ABC):
    @abstractmethod
    def details(self):
        pass

class Student(School):
    def details(self):
        print("Student name: Akshu")
s = Student()
s.details()

#14.
from abc import ABC, abstractmethod
class Music(ABC):
    @abstractmethod
    def play(self):
        pass

class Spotify(Music):
    def play(self):
        print("Playing song")
m = Spotify()
m.play()

#15.
from abc import ABC, abstractmethod
class Hospital(ABC):
    @abstractmethod
    def treatment(self):
        pass

class Doctor(Hospital):
    def treatment(self):
        print("Doctor treats patient")
d = Doctor()
d.treatment()

