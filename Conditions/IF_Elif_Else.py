# Condition provide ways to make decision in your program and execute different code base on a condition

# write a program that ask the user: Enter a number
# if the number is less than 10: Print out: Congradulation, Your number is less than 10
# if the number is greater than 10: Print out: Your number is greater than 10
# if the number is 10: print out: Congradulation, Your number is 10

number = input("Enter a number: ")
number = int(number)

if number < 10:
    print("Congradulation, Your number is less than 10")
    # this code only excute if the codition is true if it's false the next code will execute
elif number > 10:
    print("Your number is greater than 10")
else:
    print("Congradulation, Your number is", number)