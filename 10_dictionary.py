# A dictionary consists of keys and values.
# Instead of being indexed numerically like a list, dictionaries have keys.
# These keys are the keys that are used to access values within a dictionary.

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict)

# Access to the value by the key
print(Dict["key1"])

# Keys can also be any immutable object such as a tuple
print(Dict[(0, 1)])

# Each key is separated from its value by a colon ":". Commas separate the items, and the whole dictionary is enclosed in curly braces.
# An empty dictionary without any items is written with just two curly braces, like this "{}".

marks = {
    "Rohan": 35,
    "Neha": 54,
    "Sanket": 74,
    "Harry": 65,
    "Jagdish": 69,
    "Apurva": 91,
    "Amit": 45
}
print(marks)
print(marks.keys())
print(marks.values())

# .update is used to update the dictionary
# Also .update adds a key-value pair if it's not present in dictionary
marks.update({"Harry":67, "Ganesh":81})
print(marks)

print(marks.get("Dinesh")) # Prints None
# print(marks["Dinesh"]) # Returns an error

print(marks.pop("Amit")) # Removes specified key-value pair from dictionary
# Returs the value of the key being removed
print(marks)

print(marks.popitem()) # Removes last entered item from dictionary
# Returns the key-value pair that is removed
print(marks)