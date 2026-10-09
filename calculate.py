
def calculate(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'power':
        return a ** b
    elif operation == 'divide':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        return "Error: Unsupported operation"


if __name__ == "__main__":
    print(calculate(5, 3, 'add'))
    print(calculate(5, 3, 'subtract'))
    print(calculate(5, 3, 'multiply'))
    print(calculate(5, 3, 'divide'))
    print(calculate(5, 0, 'divide'))
    print(calculate(2, 3, 'power'))