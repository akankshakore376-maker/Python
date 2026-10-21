print(10 == 10.0)
print("apple" > "Apple")
print([1, 2] < [1, 2, 0])
print(True == 1, False == 0)
a = 5
print(1 < a < 10)
print(10 != 10.0)

x = 0 and 10
y = 5 and 20
print(x, y)

a = "Hello" or ""
b = "" or "World"
print(a, b)

print(not [] and not "0")

res = 10 or 1 / 0
print(res)

x = [] or [0] or False
print(x)

print(not (5 > 2 and 3 < 1))

a = True
b = False
print(a and not b or b)


a = 10
a += 5 * 2
print(a)

x = 8
x //= 3
print(x)

lst = [1, 2]
lst += [3, 4]
print(lst)

a = 5
a **= 2
print(a)

x = 12
x %= 5
print(x)

if (n := len("Python")) > 5:
    print(n)

a = 5 # 0101
b = 3 # 0011
print(a & b, a | b)

a = 5 # 0101
b = 3 # 0011
print(a ^ b)

x = 10
print(~x)

print(~(-5))

x = 3 # 0011
print(x << 2)

x = 16 # 10000
print(x >> 3)

a = 1
print((a << 3) - 1)

s = "py" in "python"
print(s)

d = {"a": 1, "b": 2}
print(1 in d, "a" in d)

print(1 not in [1, 2, 3])

t = (1, [2, 3])
print(2 in t)

print("th" not in "python")

st = {1, 2, 3}
print(3 in st)

a = [1, 2]
b = [1, 2]
print(a is b, a == b)

x = 256
y = 256
print(x is y)

m = "hello"
n = "hello"
print(m is n)

a = None
print(a is None)

p = [10]
q = p
print(p is not q)

x = True
y = 1
print(x is y)