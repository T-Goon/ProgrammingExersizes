def main():

    a = 1
    b = 1
    print("Fibonacci Series\n")

    num = int( input("How many numbers of the Fibonacci Series do you want to print? ") )

    if num == 1:
        
        print("{}".format(a))
        return 0
    
    elif num == 2:
        
        print("{}, {}".format(a, b) )
        return 0

    print("{}, {}, ".format(a, b), end="")
    a = a+b
    b = a+b

    i = 0

    # print our the series for any amount beyond 2
    while i < num:
        
        print("{}, ".format(a), end="")
        i = i + 1

        if i == (num - 2):
            
            break

        print("{}, ".format(b), end="") 
        i = i + 1

        a = a + b
        b = a + b

    return 0


if __name__ == "__main__":
    main()
