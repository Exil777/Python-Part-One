# Logical Operators are use to combine or connect boolean comparisons
# or, and, not


# Logical Operater and: Return True if both value are true
isTrue = True and True
print(isTrue)

# Logical Operater or: return True if one value is true
isNotTrue = True or False
print(isNotTrue)

# Logical Operater not: return the opposite boolean value
isNotTrue = not True
print(isNotTrue)

x = 5
y = 10

w = (x >= 4 and y > 8) 
# x is greater 4 and y is greater than 8: Variable w have a boolen value of true
print(w)


a = 3
b = 6

c = (a > 4 or y < 11)
# value a is not greater than 4 but because value y is less than 11, the or Oparetors allow c to be true because of the value y is true
print(c)




