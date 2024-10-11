# basic data structure in python: List, Tuples, Dictionaries

# List of numbers
numbers = [3, 5, 6, 7]

mixed = ["Jameson", 5, 25.24, True]
# List with many data types

print(numbers[1])
# Access element in a sequence by using indexes, and we start with 0
print(mixed[2])

print(mixed[1:2])
# Accessing a range of element by using colon: 
print(numbers[1:3])


mixed[0] = "Exil"
# modify the lyst by replacing element 0 with a different name
print(mixed)