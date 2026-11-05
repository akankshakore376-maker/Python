#SECTION 1: LIST
# 1. Remove Duplicates: Write a Python program to remove duplicate elements from a list without using set().
a = [1, 2, 3, 2, 4, 1, 5]
b = []
for i in a:
    if i not in b:
        b.append(i)
print("List after removing duplicates:", b)

# 2. Second Largest: Write a program to find the second-largest element from a list without using sort(),sorted() or max().
a = [10, 20, 30, 40, 50]
largest = second = 0
for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print("Second largest element:", second)

#3. Separate Even and Odd: Write a program to separate even and odd numbers from a list into two different lists.
a = [1, 2, 3, 4, 5, 6]
even = []
odd = []
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:", even)
print("Odd numbers:", odd)

#4. Element Frequency: Write a program to count how many times each element occurs in a list.
a = [1, 2, 2, 3, 1, 2, 4]
for i in a:
    if a.count(i) > 0:
        print(i, "occurs", a.count(i), "times")

#5. Move Zeros: Write a program to move all zeros to the end of a list without changing the order of the other elements.
a = [0, 1, 0, 3, 12]
b = []
for i in a:
    if i != 0:
        b.append(i)
for i in a:
    if i == 0:
        b.append(i)
print("List after moving zeros:", b)

#SECTION 2: TUPLE
# 6. Tuple Reversal: Write a program to reverse a tuple without using slicing.
a = (10, 20, 30, 40, 50)
b = []
for i in a:
    b.insert(0, i)
result = tuple(b)
print("Reversed tuple:", result)

#7. Maximum and Minimum: Write a program to find the maximum and minimum elements from a tuple without using built-in functions.
a = (10, 20, 5, 40, 15)
maximum = a[0]
minimum = a[0]
for i in a:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print("Maximum:", maximum)
print("Minimum:", minimum)

#8. Tuple Element Frequency: Write a program to count the occurrence of a particular element in a tuple without using the count() method
a = (10, 20, 10, 30, 10, 40)
n = 10
count = 0
for i in a:
    if i == n:
        count = count + 1
print("Occurrence:", count)

#9. Convert Tuple: Write a program to convert a tuple into a list, remove duplicate elements, and convert it back into a tuple.
a = (1, 2, 3, 2, 4, 1)
b = list(a)
c = []
for i in b:
    if i not in c:
        c.append(i)
result = tuple(c)
print("Final tuple:", result)

#10. Nested Tuple: Consider the following tuple and write a program to find the student who scored the highest marks.students = (("Amit", 85), ("Rahul", 92), ("Sneha", 78), ("Priya", 95))
students = (("Amit", 85), ("Rahul", 92), ("Sneha", 78), ("Priya", 95))
highest = students[0]
for i in students:
    if i[1] > highest[1]:
        highest = i
print("Highest scorer:", highest[0])
print("Marks:", highest[1])

#SECTION 3: SET
#11. Common Elements: Write a program to find common elements between two lists using sets
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
c = set(a) & set(b)
print("Common elements:", c)

#12. Unique Elements: Write a program to find all unique elements from two lists combined.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = set(a + b)
print("Unique elements:", c)

#13. Subset Checking: Write a program to check whether one set is a subset of another set without using the issubset() method.
a = {1, 2}
b = {1, 2, 3, 4, 5}
if a <= b:
    print("A is a subset of B")
else:
    print("A is not a subset of B")

#14. Remove Common Elements: Write a program to remove all common elements between two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a - b
d = b - a
print("Set A:", c)
print("Set B:", d)

#15. Symmetric Difference: Write a program to find elements present in either of two sets but not in both, without using the symmetric_difference() method.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = (a - b) | (b - a)
print("Symmetric Difference:", c)

#SECTION 4: DICTIONARY
#16. Character Frequency: Write a program to count the frequency of each character in a given string using a dictionary. 
a = "programming"
b = {}
for i in a:
    if i in b:
        b[i] = b[i] + 1
    else:
        b[i] = 1
print("Character Frequency:", b)

#17. Word Frequency: Write a program to count the frequency of every word in a sentence using a dictionary.
a = "python is easy and python is powerful"
b = {}
for i in a.split():
    if i in b:
        b[i] = b[i] + 1
    else:
        b[i] = 1
print("Word Frequency:", b)

#18. Highest Marks: Consider the dictionary below and write a program to find the student with the highest marks without using max().
marks = {"Amit": 85, "Rahul": 92, "Sneha": 78, "Priya": 95}
highest = 0
name = ""
for i in marks:
    if marks[i] > highest:
        highest = marks[i]
        name = i
print("Highest scorer:", name)
print("Marks:", highest)

#19. Merge Dictionaries: Write a program to merge two dictionaries. If a key exists in both dictionaries, add their values.
d1 = {"a": 10, "b": 20}
d2 = {"b": 30, "c": 40}
d = d1.copy()
for i in d2:
    if i in d:
        d[i] = d[i] + d2[i]
    else:
        d[i] = d2[i]
print("Merged Dictionary:", d)

#20. Sort Dictionary by Values: Write a program to arrange dictionary elements in ascending order based on their values without using sorted().
d = {"a": 30, "b": 10, "c": 20}
items = list(d.items())
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            items[i], items[j] = items[j], items[i]
result = dict(items)
print("Sorted Dictionary:", result)