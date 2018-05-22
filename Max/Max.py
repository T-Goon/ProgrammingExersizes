# prompt user for three numbers
num1 = input("Enter a number: ")

num2 = input("Enter a second number: ")

num3 = input("Enter a third number: ")

# find and print out the largest number
if num1 > num2 and num1 > num3:
    
    print("{} is the largest number.".format(num1))
elif num2 > num3:
    print("{} is the largest number.".format(num2))
else:
    print("{} is the largest number.".format(num3))
