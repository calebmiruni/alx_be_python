num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match case operation:
    case "+":
        result = num1 + num2
        print("The result is {result}")
    case "-":
        result = num1 - num2
        print("The result is {result}")
    case "*":
        result = num1 * num2
        print("The result is {result}")
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("The result is {result}")
    case _:
        print("Invalid operation. Please choose one of the following: +, -, *, /.")
