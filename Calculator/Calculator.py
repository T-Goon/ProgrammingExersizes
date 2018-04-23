def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def prod(a, b):
    return a * b


def div(a, b):
    return a/b


def rem(a, b):
    return a % b


def main():
    rep =1

    # Title
    print("This is a Calculator.")

    while rep == 1:
        # prompt for 2 digits and the operation
        dig1 = int(input("Enter the first digit. Press enter to continue."))

        opp = int(input("What operation would you like to preform?\n1.addition\n2.subtraction\n3.multiplication\n"
                        "4.division\n Enter the number of the operation.(EX:1)"))

        dig2 = int(input("Enter the second digit."))

        if opp == 1:
            print("{}+{}={}".format(dig1, dig2, add(dig1, dig2)))
        elif opp == 2:
            print("{}-{}={}".format(dig1, dig2, sub(dig1, dig2)))
        elif opp == 3:
            print("{}*{}={}".format(dig1, dig2, prod(dig1, dig2)))
        elif opp == 4:
            print("{}/{}={} with a remainder of {}".format(dig1, dig2, div(dig1, dig2), rem(dig1, dig2)))
        else:
            print("You have not entered a valid operation.")

        # ask if the user wants to do another calculation
        rep = int(input("Enter 1 to do another calculation"))


if __name__ == "__main__":
    main()
