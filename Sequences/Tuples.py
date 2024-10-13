# tuples are use to store multiple items in one variables: they are ordered and unachangable and they are written with round braket

fruits = ("Apples", "Oranges", "Bananas")

print(len(fruits))
# lenght of the tuple

mixed = (1, 5, "Jameson", True)
# tuples can have many data types

print(fruits[2])
# accessing and printing index 2 item of the tuple
print(fruits[-1])
# accessing and printing the last item

print(mixed[1:3])



# A tuple cannot be change but you can change the tuple into a list and change the list and change the list back into a tuple
x = ("Chery", "Apple", "Orange")
y = list(x)
y[1] = "Banana"
x = tuple(y)
print(x)
# this method can be use to add or removed an item to a tupple

del x
# deleting the tuple x

