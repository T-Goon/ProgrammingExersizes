# Recursive function to print out the natural numbers from 'i' t0 50 natural numbers
def recur(i):
    if i>50:
        return
    
    print(str(i)+", ", end="" )
    i = i+1
    
    recur(i)

def main():
    print("The first 50 natural numbers are: ", end="")
    recur(0)
    
if __name__ == "__main__":
    main()
 
