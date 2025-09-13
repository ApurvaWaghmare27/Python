# Set is a collection of non-repetitive elements
# Sets are unordered
# Sets are unindexed. Can't access elements by index value
# There is no way to change items in sets
# Sets can't contain duplicate values 
set1 = {1, 2, 3, 4, 5, 5, 5}
print(set1)

s2 = set() # Empty set declaration
print(type(s2))

# Set Methods
s2.add(123)
s2.add("Rohan")
s2.add(45)
print(s2)

print(len(s2)) # Gives number of items present in set

s2.add(False)
s2.add(22.7)
print(s2)

# s2.remove(1) # Gives error since 1 is not present in the set

print(s2.pop()) # Removes randon element from the set
# Returns the value it removed

s2.add(2)
s2.add(34)
s2.add(99)
s2.add(5)
s2.add(True)
print(s2)

s3 = {2, 3, 4, 5}
print(s2.union(s3)) # Returns a set with values from both sets combined
# Repeated values are present only once

print(s2.intersection(s3)) # Returns a set with common values from both sets

s4 = set()
s4.add("18")
s4.add(18)
print(s4)

# n = input("Enter a number: ")
# s4.add(int(n))
# print(s4)

# d = {}

# name = input("Enter your name: ")
# lang = input("Enter the language: ")
# d.update({name: lang})

# name = input("Enter your name: ")
# lang = input("Enter the language: ")
# d.update({name: lang})

# name = input("Enter your name: ")
# lang = input("Enter the language: ")
# d.update({name: lang})

# name = input("Enter your name: ")
# lang = input("Enter the language: ")
# d.update({name: lang})

# name = input("Enter your name: ")
# lang = input("Enter the language: ")
# d.update({name: lang})

# name = input("Enter your name: ")
# lang = input("Enter the language: ")
# d.update({name: lang})
# print(d)

s = {"a", "b"}
s2 = {"a"}
print(s & s2)

s3 = {"a", "a"}
print(s3)