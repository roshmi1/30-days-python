# Function to find the sum of numbers in a range divisible by both a and b
def sum_divisible_by_both(a, b, start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % a == 0 and num % b == 0:
            total_sum += num
    return total_sum

# Accept two positive integers as input
try:
    a = int(input("Enter a positive integer (a): "))
    b = int(input("Enter a positive integer (b): "))
    
    if a > 0 and b > 0:
        # Calculate the sum using the function
        result = sum_divisible_by_both(a, b, 1000, 2000)
        
        # Print the result
        if result > 0:
            print(f"The sum of numbers in [1000, 2000] divisible by both {a} and {b} is: {result}")
        else:
            print("No number found in the given range that is divisible by both a and b.")
    else:
        print("Please enter positive integers.")
except ValueError:
    print("Invalid input. Please enter positive integers.")