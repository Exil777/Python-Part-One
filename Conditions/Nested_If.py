# Write a program that check to see if a number is an even number or an odd number

number = input("Enter a number: ")
number = int(number)

if number % 2 == 0:
    # Check to see if the remainder of the division of the number is 0:
    if number == 0:
        # after checking to see if the remainder of the division of the number is 0, it's check if the actual number is 0:
        print("Number is even but it's a zero")
        # print text if the number is acually zero
    else:
        print("Your number is an even number")
        # print text if the remainder of the division is zero and the number is not actually zero
else:
    print("Your number is an odd number")
    # print text if the remainder of the division of the number is not zero