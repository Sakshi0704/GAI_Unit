def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "you are trying to divide a number by zero."


numerator = 5
denominator = 0

result = safe_division(numerator, denominator)
print(result)