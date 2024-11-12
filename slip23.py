def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary using target as auxiliary
    tower_of_hanoi(n - 1, source, target, auxiliary)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move n-1 disks from auxiliary to target using source as auxiliary
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Example usage
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'B', 'C')




Q2

import itertools

def solve_cryptarithmetic():
    # Define unique letters in the problem
    letters = 'SENDMORY'
    
    # Try all permutations of digits for these letters
    for perm in itertools.permutations(range(10), len(letters)):
        # Map letters to digits
        assignment = dict(zip(letters, perm))
        
        # Extract each letter's assigned digit
        S, E, N, D, M, O, R, Y = assignment['S'], assignment['E'], assignment['N'], assignment['D'], assignment['M'], assignment['O'], assignment['R'], assignment['Y']
        
        # Ensure no leading zeroes
        if S == 0 or M == 0:
            continue
        
        # Convert letters to numbers
        SEND = 1000 * S + 100 * E + 10 * N + D
        MORE = 1000 * M + 100 * O + 10 * R + E
        MONEY = 10000 * M + 1000 * O + 100 * N + 10 * E + Y
        
        # Check if the equation holds
        if SEND + MORE == MONEY:
            print(f"Solution found: S={S}, E={E}, N={N}, D={D}, M={M}, O={O}, R={R}, Y={Y}")
            print(f"SEND = {SEND}, MORE = {MORE}, MONEY = {MONEY}")
            return

    print("No solution found.")

# Run the solver
solve_cryptarithmetic()
