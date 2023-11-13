# Accept a positive integer as input
try:
    n = int(input("Enter a positive integer (n): "))
    
    if n > 0:
        # Generate the first n integers and join them with commas
        result = ', '.join(map(str, range(1, n+1)))
        
        # Print the result
        print(f"The first {n} integers are: {result}")
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")