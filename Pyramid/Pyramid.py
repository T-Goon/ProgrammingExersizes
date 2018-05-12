def main():
    
    height = int(input("How tall do you want the pyramid to be? "))

    # Loop for each row of pyramid
    for i in range(height):

        # Loop for the spacing of each row
        for x in range(i, height):
            print(" ",end="")

        # Loop to print the '*'s on each row
        for y in range((i*2)+1):
            print("*",end="")
        # New line at the end of each row
        print("")

        
if __name__ == "__main__":
    main()
