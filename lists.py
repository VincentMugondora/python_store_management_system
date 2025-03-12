def reverse_list_segment(input_list, start, end):
    """
    Reverses a segment of a list from the start index to the end index.
    
    Parameters:
    - input_list: The original list.
    - start: The starting index of the segment to reverse (inclusive).
    - end: The ending index of the segment to reverse (inclusive).
    
    Returns:
    - The modified list with the specified segment reversed.
    """
    # Check if indices are valid
    if start < 0 or end >= len(input_list) or start > end:
        raise ValueError("Invalid start or end index.")
    
    # Reverse the segment in place
    input_list[start:end+1] = input_list[start:end+1][::-1]
    
    return input_list

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7]
print("Original List:", my_list)
print("Reversed Segment (2 to 5):", reverse_list_segment(my_list[:], 2, 5))
