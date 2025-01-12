
def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Perform basic arithmetic operations based on the provided operation type.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The arithmetic operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float or str: The result of the operation or an error message if the operation is invalid.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'."
