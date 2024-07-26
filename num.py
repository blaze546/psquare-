def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return -1


def find_next_square(sq):
    # Calculate the square root of the given number
    root = sq ** 0.5
    
    # Check if the square root is an integer
    if root.is_integer():
        # Calculate the next perfect square
        next_square = (int(root) + 1) ** 2
        return next_square
    else:
        # If the number is not a perfect square, return -1
        return -1

# Example usage:
print(find_next_square(121))  # Output should be 144
print(find_next_square(625))  # Output should be 676
print(find_next_square(114))  # Output should be -1
