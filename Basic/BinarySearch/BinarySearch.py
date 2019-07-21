def main():
    
    # Array of values to search through
    array = [1, 1, 3, 5, 6, 8, 9, 10]
    first = 0
    middle = int(len(array)/2)
    end = len(array)

    print("Binary Search\n")

    # Prompt user for target value
    target = int(input("What value do you want to find? "))

    # Binary search algorithm to find target in list
    while first <= end:
        
        if array[middle] == target:
            
            print("The target is at index {}.".format(middle))
            return
        
        elif target > array[middle]:
            
            first = middle
            middle = int((first + end)/2)
            
        else:
            
            end = middle
            middle = int((first + end)/2)

    # Indicate if the target is not in the array
    print("The target is not in the array.") 
    return


if __name__ == "__main__":
    main()
