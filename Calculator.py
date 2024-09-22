

def addition(n1, n2):
    add = n1 + n2
    return add


def subtraction(n1, n2):
    subtract = n1 - n2
    return subtract


def multiplication(n1, n2):
    multiply = n1 * n2
    return multiply


def division(n1, n2):
    divide = n1 / n2
    return divide


calculations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


def calculator():
    print("Welcome to Calculator")
    calculator_on = True
    answer_1 = 0
    while calculator_on:
        n1 = int(input("Enter the number : "))
        still_on = True
        while still_on:
            for symbol in calculations:
                print(symbol)
            function = input("Pick an operation from the above : ")
            n2 = int(input("Enter the next number : "))
            operation = calculations[function]
            answer_1 = operation(n1, n2)
            print(f"{n1} {function} {n2} = {answer_1}")
            if input("Do you want to continue : ") == "n":
                still_on = False
                calculator_on = False
                calculator()
            n1 = answer_1


calculator()
