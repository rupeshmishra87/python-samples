class Calculator:
    """Simple Calculator class for basic arithmetic operations"""

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")


"""Adds two numbers"""


def add(one, two):
    return one + two


"""Subtracts two numbers"""


def subtract(one, two):
    return one - two


"""Multiplies two numbers"""


def multiply(one, two):
    return one * two


"""Divides two numbers"""


def divide(one, two):
    return one / two


def recursive_cal():
    operation = int(input("Enter operation type(1/2/3/4) : "))

    if 0 < operation < 5:
        one = int(input("Enter first number : "))
        two = int(input("Enter second number : "))

        if operation == 1:
            print(str(one) + " + " + str(two) + " = " + str(add(one, two)))

        elif operation == 2:
            print(str(one) + " - " + str(two) + " = " + str(subtract(one, two)))

        elif operation == 3:
            print(str(one) + " * " + str(two) + " = " + str(multiply(one, two)))

        elif operation == 4:
            print(str(one) + " / " + str(two) + " = " + str(divide(one, two)))

        recursive_cal()
    else:
        print("Invalid operation type")


if __name__ == "__main__":
    recursive_cal()
