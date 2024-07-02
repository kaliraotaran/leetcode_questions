def find_unlocking_key(lockingKey):
    # Convert the locking key to a string and get the list of digits
    digits = list(str(abs(lockingKey)))
    
    # Sort the digits
    digits.sort()
    
    # If the smallest digit is zero, find the first non-zero digit and swap
    if digits[0] == '0':
        for i in range(1, len(digits)):
            if digits[i] != '0':
                # Swap the first digit (which is zero) with the first non-zero digit
                digits[0], digits[i] = digits[i], '0'
                break
    
    # Convert the list of digits back to an integer
    unlocking_key = int(''.join(digits))
    
    # Preserve the sign of the locking key
    if lockingKey < 0:
        unlocking_key = -unlocking_key
    
    return unlocking_key

# Example usage
lockingKey = 321
print(find_unlocking_key(lockingKey))  
