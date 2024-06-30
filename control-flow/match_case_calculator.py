# User enters first number
num1 = float(input("Enter the first number: "))

# User enters the second number
num2 = float(input("Enter the second number: "))

# Choice of operation for the user
operation = ("Choose the operation, (+, -, *, /): ")

# Use match operation to perform calculations
match operation: 
    case '+' :
        result = num1 + num2
        print(f"The result is {result}.")

    case '-' : 
        result = num1 - num2
        print(f"The result is {result}.")

    case '*' :
        result = num1 * num2
        print(f"The result is {result} .") 

# Use of "if" and "else" and the error symbol to display error
    case '/' :
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result} .")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation chosen.")


