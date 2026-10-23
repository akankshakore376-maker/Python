Example 1: Print your name 4 times
for i in range(4):
    print("Akanksha")

#Example 2: Print numbers from 10 to 15
for i in range(10,16,1):
    print(i)

Example 3: Print numbers from 20 to 25
for i in range(20,26,1):
    print(i)

Example 4: Print numbers from 15 to 10 in reverse order
for i in range(15,9,-1):
    print(i)

Example 5: Print multiples of 4
for i in range(4,41,4):
    print(i)

Example 6: Print multiples of 7
for i in range(7,71,7):
    print(i)

Example 7: Print numbers from 50 to 60
for i in range(50,61,1):
    print(i)

Example 8: Print numbers in steps of 3
for i in range(10,26,3):
    print(i)

Example 9: Print the first 10 natural numbers in reverse
for i in range(10,0,-1):
    print(i)

Example 10: Print a message 6 times
for i in range(6):
    print("Hello...!",i)

Example 11: Print the multiplication table of 4
for i in range(1,11):
    print("4*",i,"=",4*i)

Example 12: Print the multiplication table of 7
for i in range(7,11):
    print("7*",i,"=",7*i)

Example 13: Find the sum of numbers from 1 to 20
sum = 0
for i in range(1,21):
    sum = sum + i
print("Total:",sum)

Example 14: Find the sum of numbers from 10 to 20
total = 0
for i in range(10,21):
    total = total + i
print("Sum :",total)

Example 15: Find the sum of multiples of 5 up to 50
total = 0
for i in range(5, 51, 5):
    total += i
print("Sum =", total)

Example 16: Print the square of numbers from 6 to 10
for i in range(6,11):
   print(i,"=",i**2)

Example 17: Print the cube of numbers from 2 to 6
for i in range(2,7):
    print(i,"=",i**3)

Example 18: Calculate the factorial of 6
fact = 1
for i in range(1,7):
    fact *= i
print("Factorial =",fact)

Example 19: Count numbers divisible by 5 from 1 to 50
total = 0
for i in range(1,51):
    if i % 5 == 0:
        total += 1
print("count :",total)

Example 20: Find the sum of squares from 1 to 5
total = 0
for i in range(1, 6):
    total += i ** 2
print("Sum of squares =", total)

Example 21: Print numbers greater than 10
for i in range(1,21):
    if i > 10:
      print(i)

Example 22: Print numbers divisible by 2 and 3
for i in range(1,31):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

Example 23: Print numbers not divisible by 2
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

Example 24: Print numbers between 10 and 30 that are divisible by 4
for i in range(10, 31):
    if i % 4 == 0:
        print(i)

Example 25: Count odd numbers from 1 to 30
count = 0
for i in range(1, 31):
    if i % 2 != 0:
        count += 1
print("Odd numbers =", count)

Example 26: Print numbers divisible by 10
for i in range(10, 101):
    if i % 10 == 0:
        print(i)

Example 27: Print numbers whose square is greater than 100
for i in range(1, 16):
    if i ** 2 > 100:
        print(i)

Example 28: Find the sum of numbers divisible by 3 from 1 to 30
sum = 0
for i in range(1,31):
     if i % 3 == 0:
          sum += i
print("Total :", sum)

Example 29: Print numbers that end in 5
for i in range(1, 101):
    if i % 10 == 5:
        print(i)

Example 30: Count numbers greater than 50
count = 0
for i in range(20,71):
    if i > 50:
        count +=1
print("Count :",count)

Example 31: Print each letter of your name
name = "Akshu"
for letter in name:
    print(letter)

Example 32: Print each character in uppercase
word = "python"
for letter in word:
    print(letter.upper())

Example 33: Print each colour in a list
colours = ["Red", "Blue", "Green", "Yellow"]
for i in colours:
    print(i)

Example 34: Print each subject in a list
subjects = ["Maths", "Science", "English", "Computer"]
for i in subjects:
    print(i)

Example 35: Find the sum of numbers in a list
numbers = [5, 10, 15, 20]
total = 0
for i in numbers:
    total += i
print("Sum =", total)

Example 36: Find the largest number in a list
numbers = [12, 45, 23, 67, 34]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest =", largest)

Example 37: Count positive numbers in a list
numbers = [-5, 10, -2, 8, 3]
count = 0
for i in numbers:
    if i > 0:
        count += 1
print("Positive numbers =", count)

Example 38: Print each number multiplied by 2
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    print(num * 2)

Example 39: Find the smallest number in a list
numbers = [18, 7, 25, 3, 14]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest =", smallest)


Example 40: Count vowels in a word
word = "computer"
count = 0
for i in word:
    if i in "aeiou":
        count += 1
print("Vowels =", count)

Example 41: Print a line of 8 stars
for i in range(8):
    print("*", end=" ")

Example 42: Print a triangle of stars
for i in range(1, 6):
    print("*" * i)

Example 43: Print an inverted triangle of stars
for i in range(5, 0, -1):
    print("*" * i)

Example 44: Print a rectangle using stars
for i in range(4):
    print("* * * * *")

Example 45: Print a number triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

Example 46: Print a triangle with repeated numbers
for i in range(1, 6):
    print(str(i) * i)

Example 47: Print the first 5 multiples of 9
for i in range(1, 6):
    print(9 * i)

Example 48: Print a countdown with a message
for i in range(5, 0, -1):
    print(i)
print("Time's up!")

Example 49: Reverse a word using a for loop
word = "Python"
reverse = ""
for i in word:
    reverse = i + reverse
print(reverse)

Example 50: Print a multiplication table of 8 in reverse order
for i in range(10, 0, -1):
    print("8 x", i, "=", 8 * i)