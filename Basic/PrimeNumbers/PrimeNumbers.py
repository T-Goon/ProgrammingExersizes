def main():

    num = int(input("Enter a number: "))

    for i in range(2,num):
        if num % i == 0:
            print("The number is not prime.")
            return 0
    print("The number is prime.")
    return 0


if __name__ == '__main__':
    main()
