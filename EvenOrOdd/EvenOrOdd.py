def EO (num):
    return num % 2 == 0

# if the number is even say so, if not say that it is not
if EO(int(input("Enter a number: "))):
    
    print("The number is even.")
    
else:
    print("The number is odd.")
