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


# List funtions
numbersTwo = [5, 3, 6, 7]

print(len(numbersTwo))
# return the lenght of the list

print(max(numbersTwo))
# return the max value in the list

print(min(numbersTwo))
# return the min value in the list


# List Methods
numbersTwo.append("rice")
print(numbersTwo)
# append elemnt to the list

print(numbersTwo.count(3))
# count how many times number 3 has appears in List numbersTwo

numbersTwo.pop()
print(numbersTwo)
# removing the last elements

names = ["Jameson", "Arron", "John", "Eve"]
names.sort()
print(names)



