#Python program to make basic calculator. It is my final version
# but it has errors when letters are input or numbers different to 1, 2, 3, 4, or 5 are input.

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        print("division by zero is not allowed, try again!")
        print()
    else:
        print(value1, "/", value2, "=", value1 / value2)
        print()
    finally:
        print("executing finally clause")
        print()

def is_letter(operation):   # Function does not work yet
    operation.isalpha()
    print()
    print("This value cannot be letters.")
    #break


finished = False
while finished == False:

    print("Hi, I am your personal calculator. I can help you with the following operations: ")

    print("Select a number:  1-Addition, 2-Subtraction, 3-Multiplication, 4-Division, 5-End")
    operation = int(input("Choose  number of operation 1, 2, 3, 4, 5 : "))


    if operation == 5:
        print()
        print("Have a good day, bye.")
        break


    if (operation >= 1) and (operation <=5):
        pass
    else:
        print()
        print("The number of the operation must be between 1 and 5.")
        break


    value1 = int(input("Enter 1st number: "))
    value2 = int(input("Enter 2nd number: "))


    if operation == 1:
        print(value1, "+", value2, "=", addition(value1, value2))
        print()

    elif operation == 2:
        print(value1, "-", value2, "=", subtraction(value1, value2))
        print()

    elif operation == 3:
        print(value1, "*", value2, "=", multiplication(value1, value2))
        print()

    elif operation == 4:
        divide(value1, value2)