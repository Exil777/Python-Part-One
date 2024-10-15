personA = {
    "name": "Jameson",
    "age": 29,
    "language": "English"
}

# using the for loop to print out the keys
for x in personA:
    print(x)

# using the for loop to print out the values 
for x in personA:
    print(personA[x])

# getting all the value with value methods with the for loop
for x in personA.values():
    print(x)

# using the for loop and the keys method to print out the keys in the dict
for x in personA.keys():
    print(x)

# using the for loop and the items method to print out the keys and the values
for x, y in personA.items():
    print(x, y)