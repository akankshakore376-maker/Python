#nested dictionary
students = {"student1": {"name": "Rahul","age": 20,"marks": 90 },"student2": {"name": "Amit", "age": 21, "marks": 85}}
print(students)

#Built in functions of dictionary
d = {1: 10, 2: 20, 3: 30}
# 1. len()
print("Length:", len(d))

# 2. str()
print("String:", str(d))

# 3. type()
print("Type:", type(d))

# 4. dict()
print("Dict:", dict(a=10, b=20))

# 5. sorted()
print("Sorted:", sorted(d))

# 6. min()
print("Minimum:", min(d))

# 7. max()
print("Maximum:", max(d))

# 8. sum()
print("Sum:", sum(d))

# 9. any()
print("Any:", any(d))

# 10. all()
print("All:", all(d))


#Methods in Dictionaries
d = {"a": 10, "b": 20, "c": 30}

# 1. clear()
x = {"a": 10}
x.clear()
print("clear:", x)

# 2. copy()
print("copy:", d.copy())

# 3. fromkeys()
print("fromkeys:", dict.fromkeys(["x", "y"], 0))

# 4. get()
print("get:", d.get("a"))

# 5. items()
print("items:", list(d.items()))

# 6. keys()
print("keys:", list(d.keys()))

# 7. values()
print("values:", list(d.values()))

# 8. pop()
x = d.copy()
print("pop:", x.pop("a"))

# 9. popitem()
x = d.copy()
print("popitem:", x.popitem())

# 10. setdefault()
x = d.copy()
print("setdefault:", x.setdefault("d", 40))

# 11. update()
x = d.copy()
x.update({"d": 40})
print("update:", x)

#Iteration
student = {"name": "Rahul","age": 20,"course": "Python"}
# for i in student.items():
#     print(i)

a = list(student.keys())
i = 0
while i < len(a):
    print(a[i], student[a[i]])
    i += 1