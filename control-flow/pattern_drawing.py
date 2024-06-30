#Ask the user to input a positive integer that represents the size of the pattern
size = input("Enter the size of the pattern:")

if 0:
    print("The size should be a number above 0. ") 

row = 0
while size: 
    for _ in range(size):
        print("*", end="")
    

