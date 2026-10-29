#1. Create a tuple containing five integers and print it.
t = (20,30,40,50,60)
print(t)

#2. Create a tuple containing a string, integer, float, and Boolean value.
s = ("Ram",23,9.20,True)
print(s)

#3. Create a single-element tuple and verify its datatype.
t = ("Ram",)
print(type(t))

#4. Print the first, middle, and last elements of a tuple.
t = ("Neha",12,23,4,True)
first, *middle, last = t
print(first)
print(middle)
print(last)

t = (10, 20, 30, 40, 50)
print("First:", t[0])
print("Middle:", t[len(t) // 2])
print("Last:", t[-1])

#5. Reverse a tuple using slicing.
t = (10,20,30,45,50)
print(t[::-1])

#6. Print every second element using slicing.
s = (10,20,30,40,50,60)
print(s[1::2])

# 7. Count how many times 25 occurs in a tuple.
s = (10,20,25,40,35,25,54)
print(s.count(25))

#8. Find the index of a given element.
t = (20,30,"Raaj",45,60)
print(t.index("Raaj"))

#9. Calculate the sum and average of numeric tuple elements.
s = (10,20,20,30,10)
print(sum(s))
print(sum(s)/len(s))

#10. Count even and odd numbers in a tuple.
s = (20,35,50,45,15,10)
even = 0
odd = 0
for i in s:
    if i%2 == 0:
        print("even",i)
        even+=1
    else:
        print("odd",i)
        odd+=1
print("Even Numbers :",even)
print("odd Numbers :",odd)

#11. Find the maximum and minimum values.
s = (20,10,5,78,4,6)
print(max(s))
print(min(s))

# 12. Check whether a particular value exists in a tuple.
t = (10, 20, 30, 40, 50)
if 30 in t:
    print("Value exists")
else:
    print("Value does not exist")

#13. Convert a list into a tuple.
t = [20,"mahi",True,35.24]
print(tuple(t))

t = (20,"mahi",True,35.24)
print(list(t))

#14. Unpack a tuple into four variables.
student = ("Rahi",23,"pune",80)
name,age,city,marks = student
print(name)
print(age)
print(city)
print(marks)

#15. Swap two variables using tuple unpacking.
a = 10
b = 20
a, b = b, a
print(a)
print(b)

#16. Access a specific value from a nested tuple.
t = ((20,"Rahi"),True,("pune",47))
print(t[2])

t = (10, 20, (30, 40, 50), 60)
print(t[2][1])

#17. Remove duplicate values while preserving order.
t = (10, 20, 10, 30, 20, 40, 30)
result = tuple(dict.fromkeys(t))
print(result)

#18. Find the second-largest distinct number.(distinct means unique(not duplicate))
t = (10, 20, 40, 30, 40, 20, 50)
unique = sorted(set(t))
if len(unique) >= 2:
    print("Second largest:", unique[-2])
else:
    print("No second-largest distinct number")


t = (10, 20, 40, 30, 40, 20, 50)
largest = max(t)
second = None
for i in t:
    if i < largest:
        if second is None or i > second:
            second = i
print("Second largest:", second)

#19. Sort a tuple in ascending order and convert the result back into a tuple.
a = (50,45,20,10,15)
print(tuple(sorted(a)))

# 20. Create a tuple of student names and marks, then print each student's details.
students = ( ("Amit", 85),("Priya", 92),("Rahul", 78),("Sneha", 95))
for name, marks in students:
    print("Name:", name,"---> ","Marks:", marks)