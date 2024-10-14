# Dictionary are use to store data in key:value pair

personA = {
    "name": "Jameson",
    "age": 29,
    "language": "English"
}

print(personA)

# dictionary Constructor 
personB = dict(name= "Exil", age= 30, country= "USA")
print(personB)

#  Value in a dict can be any data types
car = {
    "year": 2020,
    "make": "Honda",
    "model": "Accord",
    "colors": ["red", "blue", "green"]
}

print(car)

# we access the value in a dict through it's value or the get method
vehicleYear = car["year"]
print(vehicleYear)

vehicleMake = car.get("make")
print(vehicleMake)

# Key metheds gets all the keys in a dict and a values method get all values
carDictKeys = car.keys()
print(carDictKeys)

carDictValues = car.values()
print(carDictValues)


# updating dict 
car["mileage"] = 30000
print(car)

car.update({"mileage": 55000})
print(car)

# removing items in dict
car.pop("mileage")
print(car)
# removing the last items in dick
car.popitem()
print(car)
# remving item from dict
del car["model"]
print(car)
# clearing the entire dict
car.clear()
print(car)