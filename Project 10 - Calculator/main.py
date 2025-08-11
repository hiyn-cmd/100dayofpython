import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

add = add
subtract = subtract
multiply = multiply
divide = divide

calculations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculation():
    print(art.logo)
    should_keep = True
    first_num = int(input("What's the first number?: "))

    while should_keep:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        second_number = int(input("What's the second number?: "))
        result = calculations[operation](first_num, second_number)
        print(result)
        reuse = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

        if reuse == "y":
            first_num = result
        else:
            should_keep = False
            print("\n" * 20)
            calculation()

calculation()

