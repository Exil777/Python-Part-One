# Loop is programming structure that excecutes the same code over and over again as long a certain condition is met

number = 0


while number < 10:
    # # while keyword define the loop with a condition of the value of number is less than 10
    number += 1
    # if the value is less than 10: 1 is added until it reach the number 10
    print(number)


# break statement allows the ability to end a loop without caring about the conditions

x = 0

while x < 10:
    # while keyword define the loop with a condition of x less than 10
    x += 1
    # add one to x over and over until it reach 10
    if x == 5:
    # when x reach 5 the program will break 
        break
    print(x)


# continue statement allow to skip an iteration if we don't want to brake the full lop

y = 0

while y < 10:
    # while keyword define the loop with a condition of y less than 10
    y += 1
    # add one to y over and over until it reach 10
    if y == 5:
        continue
    # the program skip over 5 because of continue statement
    print(y)