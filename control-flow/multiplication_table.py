# Enter multiplication number 
number = float(input("Enter a number to see its multiplication table: "))

# Apply the range of the mulitplication
for x in range(1, 10): 
    product = number * x
    print(f"{number} * {x} = {product}")