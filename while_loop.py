#1. Print numbers from 1 to 10.
i=1
while i <= 10:
    print(i)
    i+=1

#2. Print numbers from 1 to 5.
i=1
while i <= 5:
    print(i)
    i+=1

#3. Print numbers from 10 to 1.
i=10
while i >= 1:
    print(i)
    i-=1

#4. Print even numbers from 1 to 20.
i=2
while i <= 20:
    print(i)
    i+=2

#5. Print odd numbers from 1 to 20.
i=1
while i <= 10:
    print(i)
    i+=2

#6. Print "Hello" 5 times.
i=1
while i <= 5:
    print("Hello")
    i+=1

#7. Print numbers from 5 to 15.
i=5
while i <= 15:
    print(i)
    i+=1

#8. Print multiples of 3 from 3 to 30.
i=3
while i <= 30:
    print(i)
    i+=3

#9. Print multiples of 5 from 5 to 50.
i=5
while i <= 50:
    print(i)
    i+=5

#10. Print numbers from 20 to 10.
i=20
while i >= 10:
    print(i)
    i-=1

#11. Find the sum of numbers from 1 to 10.
i=1
sum=0
while i <= 10:
    sum+=i
    i+=1
print("Total :",sum)

#12. Find the sum of numbers from 1 to 100.
i=1
sum=0
while i <= 100:
    sum+=i
    i+=1
print("Total :",sum)

#13. Find the sum of even numbers from 1 to 20.
i=2
sum=0
while i <= 20:
    sum+=i
    i+=2
print("Total :", sum)

#14. Find the sum of odd numbers from 1 to 20.
i=1
sum=0
while i <= 20:
    sum+=i
    i+=1
print("Total :",sum)

#15. Count numbers from 1 to 10.
i=1
count=0
while i <= 10:
    count+=1
    i+=1
print("Total :",count)

#16. Find the product of numbers from 1 to 5.
i=1
product=1
while i <= 5:
    product*=i
    i+=1
print(product)

#17. Print the square of numbers from 1 to 5.
i = 1
while i <= 5:
    print(i * i)
    i += 1

#18. Print the cube of numbers from 1 to 5.
i=1
while i <= 5:
    print(i**3)
    i+=1

#19. Find the sum of numbers from 1 to a user-given number.
n = int(input("Enter a number :"))
i=1
sum=0
while i <= n:
    sum+=i
    i+=1
print("Total :",sum)

#20. Count backward from a user-given number to 1.
n = int(input("Enter a number :"))
while n >= 1:
    print(n)
    n-=1

#21. Print the multiplication table of 2.
i=1
while i <= 10:
    print("2*",i,"=",2*i)
    i+=1

#22. Print the multiplication table of a user-given number.
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

#23. Print the multiplication table from 1 to 5.
n=1
while n <= 5:
    print("Table of ",n)
    i=1
    while i <= 10:
        print(n,"*",i,"=",n*i)
        i+=1
    n+=1

#24. Print the first 10 multiples of 7.
i = 1
while i <= 10:
    print(7 * i)
    i += 1

#25. Print the multiplication table in reverse order.
n = int(input("Enter a number: "))
i = 10
while i >= 1:
    print(n, "x", i, "=", n * i)
    i -= 1

#26. Find the number of digits in a number.
n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Digits =", count)

#27. Find the sum of digits of a number.
n = int(input("Enter a number: "))
total = 0
while n > 0:
    digit = n % 10
    total += digit
    n //= 10
print("Sum of digits =", total)

#28. Reverse a number.
n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
print("Reverse =", reverse)

#29. Check whether a number is a palindrome.
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

#30. Find the factorial of a number.
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial =", fact)

#31. Check whether a number is even or odd.
n = int(input("Enter a number: "))
while n >= 0:
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
    break

#32. Check whether a number is positive, negative, or zero
n = int(input("Enter a number: "))
while True:
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
    break

#33. Find the largest digit in a number.
n = int(input("Enter a number: "))
largest = 0
while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit

    n //= 10
print("Largest digit =", largest)

#34. Find the sum of odd numbers from 1 to 20.
i = 1
total = 0
while i <= 20:
    total += i
    i += 2
print(total)

#35. Check whether a number is divisible by 5.
n = int(input("Enter a number: "))
while True:
    if n % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
    break

#36. Print a star pattern.
i = 1
while i <= 5:
    print("*" * i)
    i += 1

#37. Print an inverted star pattern.
i = 5
while i >= 1:
    print("*" * i)
    i -= 1

#38. Print a number pattern.
i = 1
while i <= 5:
    print(str(i) * i)
    i += 1

#39. Print a star pattern.
i = 1
while i <= 6:
    print("*" * i)
    i += 1

#41. Print the first 10 natural numbers and their squares.
i = 1
while i <= 10:
    print(i, "Square =", i * i)
    i += 1

#42. Print numbers divisible by both 3 and 5 from 1 to 100.
i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1

#43. Print all numbers between 1 and 50 divisible by 4.
i = 1
while i <= 50:
    if i % 4 == 0:
        print(i)
    i += 1

#44. Print numbers divisible by 7
i = 1
while i <= 50:
    if i % 7 == 0:
        print(i)
    i += 1

#45. Find the sum of digits
n = 123
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)

#46. Reverse a number
n = 123
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)

#47. Print powers of 2
i = 1
while i <= 5:
    print(2 ** i)
    i += 1

#48. Print numbers that end in 5
i = 5
while i <= 50:
    print(i)
    i += 10

#49. Generate the first 5 Fibonacci numbers
a, b = 0, 1
i = 0
while i < 5:
    print(a)
    a, b = b, a + b
    i += 1

#50. Print the first 5 multiples of 9
i = 1
while i <= 5:
    print(9 * i)
    i += 1
