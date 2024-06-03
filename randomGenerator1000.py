import random
from itertools import combinations
import math

# Define the initial sequences
initial_sequences = ["3;4;6", "3;4;5", "1;2"]

# Generate all possible combinations of numbers 1 to 6
numbers = [1, 2, 3, 4, 5, 6]
min_length =   math.ceil(len(numbers) / 2) # len(numbers) #
all_combinations = []
for r in range(min_length, len(numbers) + 1):
    for comb in combinations(numbers, r):
        combination = ";".join(map(str, comb))
        if combination not in initial_sequences:
            all_combinations.append(combination)

# Determine how many sequences to generate from each list
total_sequences = 311028
half_sequences = total_sequences // 2

# Generate the sequences from the initial sequences
random_sequences = ["1;" + random.choice(initial_sequences) for _ in range(half_sequences)]

# Generate the sequences from the random combinations
random_sequences += ["0;" + random.choice(all_combinations) for _ in range(half_sequences)]

# If total_sequences is odd, add one more sequence from the random combinations
if total_sequences % 2 != 0:
    random_sequences.append("0;" + random.choice(all_combinations))

# Shuffle the combined sequences to mix them
random.shuffle(random_sequences)

# Write the sequences to a file
with open("random_sequences.txt", "w") as file:
    for sequence in random_sequences:
        file.write(sequence + "\n")

print("Random sequences generated and saved to random_sequences.txt")
