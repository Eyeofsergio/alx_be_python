# Safe divide class

def safe_divide(numerator, denominator):
    
    try:
        num = float(numerator)
        denom = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."
        result = numerator/denominator
        return f"The result of the division ia {result}"
    except ValueError:
        return "Error: Please enter numeric values only."