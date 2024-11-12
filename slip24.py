def sort_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Sort the words alphabetically (case-insensitive)
    words.sort(key=str.lower)
    # Join the sorted words back into a sentence
    sorted_sentence = " ".join(words)
    return sorted_sentence

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
sorted_sentence = sort_sentence(sentence)
print("Original Sentence:", sentence)
print("Sorted Sentence:", sorted_sentence)


Q2



import itertools

def solve_cryptarithmetic():
    # Define unique letters in the problem
    letters = 'CROSSDANGER'
    
    # Try all permutations of digits for these letters (without duplicate values)
    for perm in itertools.permutations(range(10), len(set(letters))):
        # Map letters to digits
        assignment = dict(zip(set(letters), perm))
        
        # Extract each letter's assigned digit
        C = assignment['C']
        R = assignment['R']
        O = assignment['O']
        S = assignment['S']
        D = assignment['D']
        A = assignment['A']
        N = assignment['N']
        G = assignment['G']
        E = assignment['E']

        # Ensure no leading zeroes
        if C == 0 or R == 0 or D == 0:
            continue
        
        # Convert letters to numbers for CROSS, ROADS, and DANGER
        CROSS = 10000 * C + 1000 * R + 100 * O + 10 * S + S
        ROADS = 10000 * R + 1000 * O + 100 * A + 10 * D + S
        DANGER = 100000 * D + 10000 * A + 1000 * N + 100 * G + 10 * E + R
        
        # Check if the equation holds
        if CROSS + ROADS == DANGER:
            print(f"Solution found: C={C}, R={R}, O={O}, S={S}, D={D}, A={A}, N={N}, G={G}, E={E}")
            print(f"CROSS = {CROSS}, ROADS = {ROADS}, DANGER = {DANGER}")
            return

    print("No solution found.")

# Run the solver
solve_cryptarithmetic()
