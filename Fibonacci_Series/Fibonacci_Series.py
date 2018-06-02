def main():

    a = 1
    b = 1
    print("Fibonacci Series\n")

    # prompt user for input
    num = int(input("How many numbers of the Fibonacci Series do you want to print? "))

    # if the input is 1 or 2 print it out and then exit
    if num == 1:
        print("{}".format(a))
        return 0
    elif num == 2:
        print("{}, {}".format(a, b))
        return 0

    # print out the first 2 in series when input is more than 2 and recalculate 'a' and 'b'
    print("{}, {}, ".format(a, b), end="")
    a = a+b
    b = a+b

    # counter variable
    i = 0

    # loop to print our the series for any amount beyond 2
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
