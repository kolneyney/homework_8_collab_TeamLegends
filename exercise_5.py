def reverse_ascending(numbers):
    if numbers == []:
        return []
    
    # Create an empty list for putting reverse ascending subsequences
    reverse_numbers = []
    
    # Subsequence (the reversed) should be initiate with the first elements of input list
    subsequence = [numbers[0]]
    
    for i in range(1, len(numbers)):
        
        # If current number is greater than the previous number, add to the ascending subsequence
        if numbers[i] > numbers[i-1]: 
            subsequence.append(numbers[i])
            
        # If current number is not greater than the previous number, it marks as the end of the ascending subsequence
        else:
            reverse_numbers.extend(reversed(subsequence))   # Reverse the subsequence and add it to the result
            subsequence = [numbers[i]]   # Start a new subsequence with the current number again, same process
    
    reverse_numbers.extend(reversed(subsequence))   # Add ascending subsequence to the result

    return reverse_numbers


            
            
            