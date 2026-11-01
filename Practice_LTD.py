1. Create a list of 5 numbers and print it.
num = [10,20,"Aman","Raaj"]
print(num)

2.Print the first element of a list.
n = [12,34,"Nisha",6.5]
print(n[0])

3. Print the last element of a list.
a = [23,9,"Akshu",60]
print(a[-1])

4. Find the length of a list.
a = [12,"deepa",True,4.5]
print(len(a))

5.Add an element to a list.
b = [18.30,45,"Abhi",56]
b.append(23)
print(b)

6.Insert an element at a specific position.
s = [56,67,"Manu",90,"Reena"]
s.insert(1,20)
print(s)

7. Remove an element from a list.
a = [20,"Neta",67,"hello",58]
a.remove("hello")
print(a)

8. Remove the last element from a list.
b = [40,59,"Tanuj",6.9,80]
b.pop()
print(b)

9. Find the maximum number in a list.
s = [20,50,34,67,87]
print(max(s))

10. Find the minimum number in a list.
a =[20,49,10,49,4]
print(min(a))

11. Find the sum of all list elements.
c = [2,4,7,8,9]
print(sum(c))
 
12. Sort a list in ascending order.
a =[20,49,10,49,4]
a.sort()
print(a)

13. Sort a list in descending order.
a =[27,79,10,59,4]
a.sort(reverse=True)
print(a)

14. Reverse a list.
s = [23,"Anita",76,80]
s.reverse()
print(s)

15. Count how many times an element appears.
s = [28,45,48,23,67,23]
print(s.count(23))

16. Check whether an element exists in a list.
a = [44,76,56,78,29]
if 56 in a:
    print("Element Exist")
else:
    print(" Element Not Exit")

17. Print all elements using a for loop.
a = [45,"hello",76,"Python"]
for i in a:
    print(i)

18. Find even numbers from a list.
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in a:
    if i % 2 == 0:
        print("Even --->",i)

19. Find odd numbers from a list.
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in a:
    if i % 2 == 1:
        print("Odd number --->",i)

20. Remove duplicate elements from a list.
s = [28,45,48,23,67,23]
result = []
for i in s:
    if i not in result:
        result.append(i)
print(result)

21. Create a tuple and print it.
t = (2,4,"akash",True)
print(t)

22. Print the first element of a tuple.
t = (2,4,"akash",True)
print(t[0])

23. Print the last element of a tuple.
t = (2,4,"akash",True)
print(t[-1])

24. Find the length of a tuple.
t = (2,4,"akash",True)
print(len(t))

25. Count occurrences of an element.
t = (2,4,7,9,4)
print(t.count(4))

26. Find the index of an element.
t = (2,4,7,9,4)
print(t.index(7))

27. Check whether an element exists in a tuple.
t = (22,40,7,9,55,23)
if 9 in t:
    print("Element Exist")
else:
    print("Element Not Exist")

29. Find the minimum element in a tuple.
t = (22,40,7,9,55,23)
print(min(t))

30. Find the sum of tuple elements.
t = (22,40,7,9,55,23)
print(sum(t))

31. Convert a tuple into a list.
t = (22,40,7,9,55,23)
print(list(t))

32. Convert a list into a tuple.
a = [20,"Raam",78,54,0]
print(tuple(a))

33. Print all tuple elements using a loop.
t = (22,40,7,9,55,23)
for i in t:
    print(i)

34. Concatenate two tuples.
t1 = (1,2,3)
t2 = (4,5,6)
print(t1 + t2)

a = (10, 20, 30)
b = (40, 50, 60)
c = a + b
print(c)

35. Find even numbers from a tuple.
a = (10, 25,67,78, 30)
for i  in a:
    if i % 2 == 0:
        print("Even:" ,i)

36. Create a dictionary and print it.
d = {"age":23,"name":"Asha","city":"Belagavi"}
print(d)

37. Access the value of a key.
d = {"age":23,"name":"Asha","city":"Belagavi"}
print(d["name"])

38. Add a new key-value pair.
student = {"name": "Rahul","age": 20}
student["city"] = "Pune"
print(student)

39. Update the value of an existing key.
student = {"name":"Asha","city":"Belagavi","age":23}
student["city"] = "Pune"
print(student)

40. Delete a key from a dictionary.
student = {"name": "Rahul","age": 20,"city": "Pune"}
del student["age"]
print(student)

41. Find the number of items in a dictionary.
student = {"name": "Rahul","age": 20,"city": "Pune"}
print(len(student))

#42. Print all dictionary keys.
student = {"name": "Rahul","age": 20,"city": "Pune"}
print(student.keys())

#43. Print all dictionary values.
student = {"name": "Rahul","age": 20,"city": "Pune"}
print(student.values())

#44. Print all keys and values.
student = {"name": "Rahul","age": 20,"city": "Pune"}
print(student.items())

#45. Check whether a key exists in a dictionary.
student = {"name": "Rahul","age": 20,"city": "Pune"}
if "name" in student:
    print("key exist")
else:
    print("key not exist")

#46. Merge two dictionaries.
a = {"name":"Megha","age":23}
b = {"city":"Belagum","marks":80}
a.update(b)
print(a)

#47. Find the maximum value in a dictionary.
marks = {"Rahul": 80,"Amit": 90,"Priya": 95}
print(max(marks.values()))

#48. Find the minimum value in a dictionary.
marks = {"Rahul": 80,"Amit": 90,"Priya": 95}
print(min(marks.values()))

#49. Count the frequency of each character in a string.
text = "banana"
result = {}
for i in text:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)

#50. Create a dictionary from two lists.
keys = ["name", "age", "city"]
values = ["Rahul", 20, "Pune"]
result = dict(zip(keys, values))
print(result)