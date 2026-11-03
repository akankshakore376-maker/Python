s = {23,45,65,60}
print(s)

#set oeratipn
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
print(a ^ b)  # Symmetric difference

#set empty()
s = set()

#len
a = {10, 20, 30, 20, 10}
print(len(a))

#methods
#1.add()
s = { 10,20,30,40,50}
s.add(60)
print(s)

#2.update()
s = {1,2,3}
s.update([4,5])
print(s)

#3.remove()
s = {20,30,25,50}
s.remove(25)#Note: Gives a KeyError if the element does not exist.
print(s)

#4.discard()
s = {20,30,25,50}
s.discard(50)
print(s)

s = {20,30,25,50}
s.discard(35)#Note: No error if the element does not exist.
print(s)

#5.pop()
s = {10, 20, 30}
x = s.pop()#The removed element is not guaranteed.
print(x)
print(s)

#6.clear()
s = {1,2,3}
s.clear()
print(s)

#7.copy()
s = {2,34,5}
a = s.copy()
print(a)

#8. union() – Combine two sets
a = {1,2,3}
b = {4,5,6}
print(a.union(b))

#9.intersection() – Find common elements
a = {1,2,3}
b = {3,4,5}
print(a.intersection(b))

#10.difference() – Find elements present only in the first set
a = {1,2,3}
b = {3,4,5}
print(a.difference(b))

#11.symmetric_difference() – Find elements that are not common
a = {1,4,3}
b = {3,4,5}
print(a.symmetric_difference(b))

#12. issubset() – Check whether one set is a subset of another
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))

#13. issuperset() – Check whether a set contains another set
a = {1, 2, 3, 4}
b = {1, 2}
print(a.issuperset(b))

#14. isdisjoint() – Check whether two sets have no common elements
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))


#frozenset
# frozenset is an immutable version of a set.
#you cannot add, remove, or modify elements after creating it.
a = frozenset([1, 2, 3, 4, 5])
print(a)
