# Lists are mutable in Python
# Unlike Strings, Lists are mutable

list1 = ["apple", 3.14, "orange", 89, False, "Rohan"]
print(list1[0])
print(list1[4])
print(list1[2])

print(list1)
print(type(list1))
print(len(list1))

print(list1[3])
list1[3] = "69"
print(list1[3])

# List slicing
print(list1[1:4])

# List Methods
list2 = [2, 34, 12, 5, 45, 3]
list2.sort() # Sorting the list

# now list2 is [2, 3, 5, 12, 34, 45]
print(list2)
print(list2[2])
print(list2[1:4])

list2.reverse() # Gives list in reverse format

# now the list2 is [45, 34, 12, 5, 3, 2]
print(list2)
print(list2[2])
print(list2[3:])

list2.append(9) # Adds 9 at the end of the list
print(list2)

list2.insert(3, 333) # Insert 333 in list2 such that its index is 3
print(list2[3])
print(list2)

list2.remove(12) # Removes specified element(12) from the list
print(list2)

print(list2[2]) 
print(list2.pop(2)) # Pops out element at index 2 from list2
print(list2)

# List Nesting
# A list can contain tuple as part of its elements
nesting = [1, 22, ["Rohan", "Rohit"], 3.14, False, ["CS", "IT", "ENTC"], True, "Sanket", (1, 2, 3)]
print(type(nesting)) # list
print(len(nesting)) # 9 elements

print(nesting[2]) # Gives elements at 2nd index
print(nesting[2][0]) 
print(nesting[2][1])

print(nesting[5][0]) # Gives element at 5th index
print(nesting[5][1])
print(nesting[5][2])

print(type(nesting[8])) # Gives type of elements at index 8

nesting.extend(["pop", 69]) # Adds elements at the end of the list named nesting
print(nesting)

nesting.append("A") # Adds element at the end of the list
print(nesting)

# Convert string into list
list3 = "Dwayne Johnson".split() # Splits the string into two different elements of a list
print(list3)

list4 = "A,B,C,D,E".split(",") # ',' is a Delimiter here
print(list4)

print([1,2,3] + [1,1,1])

# Difference between Append and Extend methods
A = [1]
A.append([2,3,4,5]) # append adds [2,3,4,5] as a single element in the list
A.extend([6,7]) # extend adds 6 & 7 as two different elements in the list
print(len(A))

# Clone a list
print("A:", A)
B = A[:]
print("B:", B)
del(B[1])
print("A:", A)
print("B:", B)

l1 = ["banana", 3.14, False]
l2 = l1 # This is not proper cloning
# When we set one variable l2 equal to l1, both l1 and l2 are referencing the same list in memory
print("l1:", l1)
print("l2:", l2)

# As l1 and l2 are referencing the same list, if we change list l1, then list l2 also changes.
l1[0] = "Orange"
print("After change:")
print("l1:", l1)
print("l2:", l2)