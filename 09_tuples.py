# Tuple is immutable in Python
t1 = (12, 3, 23, 56, 4)
print(type(t1))
print(len(t1))
print(t1)

t2 = () # Empty tuple
print(t2)

t3 = (1,) # Tuple with 1 element
print(t3)

t4 = (1, 45, "Rohan", 33.33, False, "Rohit")
# t4[0] = 23 we can't change elements of a Tuple
print(t4)

# Tuple Methods
t5 = (1, 45, "Rohan", 33.33, False, "Rohit", 45)
print(t5.count(45)) # Gives the count of the occurance of an element in tuple

print(t5.index(33.33)) # Gives index value of the element

t6 = t5 + t1 # Tuple Concatenation
print(t6)

print(t5) # tuples are immutable 
print(t1) # Original tuple remains the same

print(t6)
# We can check if an element present in a tuple or not
# using 'in' keyword
print(1 in t6)
print(27 in t6)


# Unpacking tuples
t7 = (1, 2, 3)
a, b, c = t7
print(a, b, c)

# min() and max() function gives the smallest and largest element in a tuple
t8 = (23, 12, 22.7, 9, 67)
print(min(t8))
print(max(t8))

print(sum(t8)) # sum() gives the sum of all tuple elements

# Tuple Nesting
# A tuple can contain a list as part of its elements
nesting = (1, 23, ["Rohan", "Rohit"], 22.7, ("IT", "CS", "ENTC"), False, True, 0)
print(type(nesting))
print(len(nesting))

print(nesting[2]) # Gives 2nd index element
print(type(nesting[2]))
print(nesting[2][0])
print(nesting[2][1])

print(nesting[4]) #Gives 4th index element
print(type(nesting[4]))
print(nesting[4][0])
print(nesting[4][1])
print(nesting[4][2])

tuple1 = (0, 1, 2, 3, 10, 56, 34, 3, 9, 4, 38, 22, 69)
tuple2 = sorted(tuple1)
print(tuple2)

# Very Important
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print("Element 0 of Tuple:", NestedT[0])
print("Element 1 of Tuple:", NestedT[1])
print("Element 2 of Tuple:", NestedT[2])
print("Element 3 of Tuple:", NestedT[3])
print("Element 4 of Tuple:", NestedT[4])

print("Element 2, 0 of Tuple:",   NestedT[2][0])
print("Element 2, 1 of Tuple:",   NestedT[2][1])
print("Element 3, 0 of Tuple:",   NestedT[3][0])
print("Element 3, 1 of Tuple:",   NestedT[3][1])
print("Element 4, 0 of Tuple:",   NestedT[4][0])
print("Element 4, 1 of Tuple:",   NestedT[4][1])

print("Element 2, 1, 0 of Tuple:",   NestedT[2][1][0])
print("Element 2, 1, 1 of Tuple:",   NestedT[2][1][1])