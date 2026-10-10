
def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'power':
        return a ** b
    elif operation == 'modulo':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a % b
    elif operation == 'floor_divide':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a // b
    elif operation == 'minimum':
        return min(a, b)
    elif operation == 'maximum':
        return max(a, b)
    elif operation == 'absolute':
        return abs(a)
    elif operation == 'average':
        return (a + b) / 2
    elif operation == 'square':
        return a ** 2
    elif operation == 'cube':
        return a ** 3
    elif operation == 'square_root':
        if a < 0:
            return "Error: Cannot take square root of a negative number"
        return a ** 0.5
    elif operation == 'divide':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        return "Error: Unsupported operation"


if __name__ == "__main__":
    print(calculator(5, 3, 'add'))
    print(calculator(5, 3, 'subtract'))
    print(calculator(5, 3, 'multiply'))
    print(calculator(5, 3, 'divide'))
    print(calculator(5, 0, 'divide'))
    print(calculator(2, 3, 'power'))