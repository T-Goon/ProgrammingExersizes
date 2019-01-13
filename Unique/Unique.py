# Prompt user for how many elements to add to the list

size = int(input("Enter the number of elements to be stored in the array: "))

# Initialize the list
list = list()

# Have the user fill the list
for i in range(0, size):
    list.append(input("Enter element {}: ".format(i)))

# Print out each unique element in the list
print("The unique elements in the list are: ", end="")
for i in range(0, size):
    if list.count(list[i]) == 1:
        print("{}, ".format(list[i]), end="")
