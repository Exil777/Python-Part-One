# Input function allow us to get input from the console application


# What is the user Current age

userName = input("Enter your name?: ")
# asking the user to enter a name as an input
birthYear = input("What year where you born?: ")
birthYear = int(birthYear)
# asking the user to enter his birth year as an input put and typecast the variable from str to int
currentYear = input("What is the current year?: ")
currentYear = int(currentYear)
# asking the user to enter his current year as an input put and typecast the variable from str to int


currentAge = currentYear - birthYear
# calc user age and assign the value to a variable name currentAge

print(userName, "You are:", currentAge, "Years old")
