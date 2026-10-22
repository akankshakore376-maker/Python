month = 5
match month:
    case 1|2|3:
        print("First Quater")
    case 4|5|6:
        print("Second Quater")
    case 7|8|9:
        print("Third Quader")
    case 10|11|12:
        print("Fourth Quater")
    case _:
        print("Invalid Month")


num1 = int(input("First number:"))
num2 = int(input("Second number:"))
op = input("Enter operator(+,-,*,/,**):")
match op:
    case "+":
        print("Addtion:",num1+num2)
    case "-":
        print("Subtract:",num1-num2)
    case "*":
        print("Multiplication:",num1*num2)
    case "/":
        print("Division:",num1/num2)
    case "**":
        print("Exponesion:",num1**num2)
    case _:
        print("Invalid choice")



Check a vowel
choice = input("Enter a character: ").lower()
match choice:
    case "a":
        print("Vowel")
    case "e":
        print("Vowel")
    case "i":
        print("Vowel")
    case "o":
        print("Vowel")
    case "u":
        print("Vowel")
    case _:
        print("Not a vowel")



Check the day of the week
day = int(input("Enter a number (1-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")



Check a traffic light signal
signal = input("Enter traffic signal color: ").lower()
match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")



Check positive or negative number
num = int(input("Enter a number: "))
match num:
    case n if n > 0:
        print("Positive number")
    case n if n < 0:
        print("Negative number")
    case _:
        print("Zero")

    
Check whether a person is eligible to vote
age = int(input("Enter your age: "))
match age:
    case a if a >= 18:
        print("Eligible to vote")
    case a if a < 18 and a >= 0:
        print("Not eligible to vote")
    case _:
        print("Invalid age")


Check even or odd number
num = int(input("Enter a number: "))
match num:
    case n if n % 2 == 0:
        print("Even number")
    case n if n % 2 != 0:
        print("Odd number")  


#grade
marks = 85
match marks:
    case 1 | 2 | 3 | 4 | 5:
        print("Grade F")
    case 6 | 7:
        print("Grade C")
    case 8:
        print("Grade B")
    case 9 | 10:
        print("Grade A")
    case _:
        print("Invalid marks")

