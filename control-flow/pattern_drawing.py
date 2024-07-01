#Ask the user to input a positive integer that represents the size of the pattern
size = int(input("Enter the size of the pattern: "))

if size <= 0:
    print("The size should be a number above 0. ") 

row = 0
for row in range(size): 
    for _ in range(size):
        print("*", end="")
    

