def find_dot_sequence(lst, dot_index):
    seq, curr = 0, -1
    for i, item in enumerate(lst):
        if item == '.':
            if curr == -1: curr, seq = seq, seq + 1
        else:
            curr = -1
        if i == dot_index: return curr
    return -1

# Example usage
lst = ['1', '.', '.', '2', '.', '.', '.', '3', '.']
dot_index = 4  # Example: we want the sequence of the dot at index 4
result = find_dot_sequence(lst, dot_index)
print(f"The dot at index {dot_index} belongs to sequence {result}.")
