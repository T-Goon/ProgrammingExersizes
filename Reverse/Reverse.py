# Prompt user for text
txt = input("Enter some text: ")

# Print out text backwards
for i in range(len(txt)-1, -1, -1):
    
    print(txt[i], end="")
