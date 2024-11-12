import string

def remove_punctuation(input_string):
    # Define the translation table that removes punctuation
    translator = str.maketrans('', '', string.punctuation)
    # Remove punctuation from the string
    return input_string.translate(translator)

# Example usage
input_string = "Hello, World! This is a test string with punctuations: commas, periods, etc."
output_string = remove_punctuation(input_string)
print("Original String:", input_string)
print("String without Punctuation:", output_string)


Q2

import itertools

def solve_cryptarithmetic():
    # Define letters and all possible digit combinations
    letters = 'GOTU'
    digits = range(10)
    
    # Try all possible digit assignments to G, O, T, and U
    for perm in itertools.permutations(digits, len(letters)):
        # Create a dictionary to map each letter to a digit
        assignment = dict(zip(letters, perm))
        
        # Extract the digits assigned to each letter
        G, O, T, U = assignment['G'], assignment['O'], assignment['T'], assignment['U']
        
        # Ensure the first letters are not zero (leading zeros are not allowed)
        if G == 0 or T == 0 or U == 0:
            continue
        
        # Convert letters to numbers using the current assignment
        GO = 10 * G + O
        TO = 10 * T + O
        OUT = 100 * O + 10 * U + T
        
        # Check if the equation is satisfied
        if GO + TO == OUT:
            print(f"Solution found: G={G}, O={O}, T={T}, U={U}")
            print(f"GO = {GO}, TO = {TO}, OUT = {OUT}")
            return

    print("No solution found.")

# Run the solver
solve_cryptarithmetic()
