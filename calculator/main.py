from art import logo
import math

#Define calculator operations
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def exponentiate(n1, n2):
    return n1 ** n2


def sqrt(n1):
    return math.sqrt(n1)



operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponentiate,
    "square root": sqrt,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    end_calculation = False

    while not end_calculation:
        symbol = input("Pick an operation: ")
        if symbol == "square root":
            answer = operations[symbol](num1)
            print(f"The square root of {num1} is {answer}")
        else:
            num2 = float(input("What's the next number?: "))
            answer = operations[symbol](num1, num2)
            print(f"{num1} {symbol} {num2} = {answer}")

        to_continue = ""
        while to_continue == "":
            to_continue = input("Would you like to continue calculating? Type 'y' or 'n' to start new calculation: ").lower()

            if to_continue == 'y':
                num1 = answer
                end_calculation = False
            elif to_continue == 'n':
                end_calculation = True
                calculator()
            else:
                print("Please pick a valid option")
                to_continue = ""


calculator()