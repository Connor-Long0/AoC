# Goal: create program that finds total distance between two lists
# Steps:
# 1. Load file in
# 2. Create lists out of both with for loop, and convert to int
# 3. Subtract left FROM right, abs, and += to variable total, loop until finished

with open(r'C:\Users\19164\Desktop\AoC\2024\numbers.txt', 'r') as file:

    # Set left, right to empty arrays, get total ready to use
    left = []
    right = []
    total = 0

    # Create lists out of both sides via append
    for lines in file:
        fields = lines.split()
        left.append(int(fields[0]))
        right.append(int(fields[1]))

    # Sort both lists, and overwrite
    left = sorted(left)
    right = sorted(right)
    
    # Loop adding absolute value of distance to the length of the left side as both sides are the same length
    for i in range(len(left)): 
        total += abs(left[i] - right[i])

    # Final answer
    print(total)