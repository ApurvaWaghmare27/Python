#Assignment Operators
a = 7 # = is a assignment operator
print(a)

a += 1 
print(a) # += is a assignment operator

a -= 2
print(a) # -= is a assignment operator

# Arithmetic Operators 
# +, -, *, /, % these are arithmetic operators
a = 12
b = 6
c = a+b
print(c)

print(a-b)
print(a*b)
print(a/b)
print(a%b)

compare = 5<4
print(compare)
print(not(compare)) # Not operator makes false-->true and true-->false

a = 2
print(a**2) # prints square of a number
print(a**3) # prints cube of a number

s = 0.0 and "Apurva"
print(s) # Output: False which is 0.0 in this case

# Logical AND
# a and b
# The result is a if a is false(0, 0.0, 0+0j, empty string, tuple, list)
# Otherwise the result is b

a = 0.0 and 1+2j
print(a)

a = 12 and 1+3j
print(a)

a = "Apurva" and "Waghmare"
print(a)

a = 12.0 and 0
print(a)

# Logical OR
''' a or b
The result is a when a is True
otherwise the result is b '''

b = 10 or 0
print(b) # 10

b = 0 or 2+4j
print(b) # 2+4j

b = "apurva" or "waghmare"
print(b) # apurva

b = "" or "Rohan"
print(b) # Rohan

# Logical NOT
c = not("Apurva")
print(c) # False

c = not(0+0j)
print(c) # True

c = not(12)
print(c) # False

c = not(0.0)
print(c) # True

