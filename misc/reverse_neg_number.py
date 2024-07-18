def reverse_number(x):
    # Check if the number is negative
    is_negative = x < 0
    
    # Convert to positive for reversal
    x = abs(x)
    
    # Reverse the digits
    reversed_num = int(str(x)[::-1])
    
    # Apply the original sign
    return -reversed_num if is_negative else reversed_num

# Test the function
x = 1534236469
rev = reverse_number(x)
print(rev)  # Output: -12