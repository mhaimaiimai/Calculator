def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    num1 = float(input("What's the first number?: "))
    is_calcend = False
    while (not is_calcend):
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        if operator in operations:
            calcfunction = operations[operator]
            result = calcfunction(num1, num2)
            print(f"{num1} {operator} {num2} = {result}")
            chkcon = input(
                f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: "
            )
            if chkcon == "y":
                num1 = result
            else:
                is_calcend = True
        else:
            print("Please try again with valid operator.")


calculator()
