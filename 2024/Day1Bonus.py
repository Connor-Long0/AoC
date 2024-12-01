# Goal: create program that finds total similarity score between lists
# Steps:
# 1. Load file in
# 2. Create lists out of both with for loop, and convert to int
# 3. Dictionary that allows to see matches from the left side to the right side, then multiply the left num by matches

with open(r'C:\Users\19164\Desktop\AoC\2024\numbers.txt', 'r') as file:

    # Set left, right to empty arrays, get total ready to use
    left = []
    right = []
    sim_score = 0

    # Create lists out of both sides via append
    for lines in file:
        fields = lines.split()
        left.append(int(fields[0]))
        right.append(int(fields[1]))

    # Sort both lists, and overwrite
    left = sorted(left)
    right = sorted(right)
    
    # Sets a right count dictionary, and gets each num, checks with left
    right_count = {}
    for num in right:
        right_count[num] = right_count.get(num, 0) + 1

    # Check to see if in left, if so, multiplies the original number by right count, which is now set to the number of matches to num
    for num in left:
        sim_score += num * right_count.get(num, 0)
    
    # Prints the final similarity score
    print(sim_score)