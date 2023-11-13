# Function to calculate the sum of digits in a number
def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)
    
    # Initialize sum to 0
    digit_sum = 0
    
    # Iterate through each digit and add it to the sum
    for digit in num_str:
        digit_sum += int(digit)
    
    return digit_sum

# Accept a positive integer as input
try:
    input_number = int(input("Enter a positive integer: "))
    
    if input_number > 0:
        # Calculate the sum of digits using the function
        result = sum_of_digits(input_number)
        
        # Print the result
        print(f"The sum of digits in {input_number} is: {result}")
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")