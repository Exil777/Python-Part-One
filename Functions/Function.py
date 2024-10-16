# function are organized codes that be use at different places in our script

def hello():
    # defing a fuction with the def key and name the fucnction hello
    print("Hello")

hello()
# calling the function

def print_sum(num1, num2):
    # defining a fuction call print_sum with two parameters that we can process in our code
    print(num1 + num2)

print_sum(10, 20)


def add(num1, num2):
    return num1 + num2
    # intead of automatically executing a code with return a value that can be use later
num3 = add(20, 30)
print(num3)