# Function to find and print factors of a number
def print_factors(number):
    print(f"The factors of {number} are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

# Accept a positive integer as input
try:
    n = int(input("Enter a positive integer (n): "))
    
    if n > 0:
        # Print factors using the function
        print_factors(n)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")