def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "can't divide by 0"

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    num1 = float(input("What is the first number?"))
    continue_calc = True

    while continue_calc:
        for i in operations:
            print(i)
        operation_symbol = input("Type an operation from above")
        num2 = float(input("What is the second number?"))
        function = operations[operation_symbol]
        answer = function (num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_calc_choice = input("Should continue? y for yes, n for no").lower()
        if continue_calc_choice == "n":
            continue_calc = False
            calculator()
        else:
            num1 = answer
calculator()