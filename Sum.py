# prompt user for the size of the list
size = int(input("Enter the size of the array: "))

# initialize list
array = list()

# fill list with "size" number of elements
for i in range(0, size):
    array.append(int(input("Enter element {}: ".format(i))))

# calculate the sum of the elements
sum = 0
for i in array:
    sum = sum + i

# print out the sum
print("The sum of all elements in the array is {}.".format(sum))
