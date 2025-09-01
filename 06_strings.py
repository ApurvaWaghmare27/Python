# Strings in Python
# Strings are immutable in Python

name = "apurva"
print(len(name)) # gives the count of number of characters in the string

# String slicing
slice = name[0:3]
print(slice)

print(name[:4])
print(name[3:])
print(name[-4:-1]) # this is negative indexing

# String functions
firstName = "Apurva"
lastName = "Waghmare"
fullName = firstName + lastName # String Concatenation
print(fullName)

print(lastName.endswith("are"))
print(lastName.startswith("z"))

letter = '''Dear <|Name|>
You are selected!
<|Date|>'''
newLetter = letter.replace("<|Name|>", "Apurva").replace("<|Date|>", "16 Sept 2030")
print(newLetter)

name = "i am Iron Man"
print(len(name))
print(str.capitalize(name)) # makes first letter capital and rest small
print(str.upper(name)) # makes every letter capital
print(str.lower(name)) # makes every letter small
print(str.title(name)) # makes first letter of every word capital

name = "My name is  Apurva"
print(name.find("  "))
print(name.find("rva"))
print(name.replace("  ", " "))

# f-String in Python
name2 = input("Enter your name: ")
print(f"Good Morning! {name2}")