#1. Fibonacci Series
#A Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers.
n = int(input("Enter terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


#2. Palindrome Number
#A palindrome number is a number that remains the same when its digits are reversed.
n = int(input("Enter number: "))
temp = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


#3. Armstrong Number
#An Armstrong number is a number that is equal to the sum of its digits, each raised to the power of the total number of digits.
n = int(input("Enter number: "))
temp = n
total = 0
while n > 0:
    digit = n % 10
    total = total + digit ** 3
    n = n // 10
if temp == total:
    print("Armstrong")
else:
    print("Not Armstrong")


#4. Prime Number
#A prime number is a number greater than 1 that has exactly two factors: 1 and itself.
n = int(input("Enter number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
if n > 1 and count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")
