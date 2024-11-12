class CollegeInfoBot:
    def __init__(self):
        self.info = {
            "name": "Alex Johnson",
            "college": "XYZ University",
            "department": "Computer Science",
            "year": "Third Year",
            "gpa": 3.8,
            "upcoming_events": ["Tech Fest on Nov 20", "Sports Day on Dec 15", "Annual Day on Jan 5"],
            "timetable": {
                "Monday": "Math, Data Structures, Computer Networks",
                "Tuesday": "Physics, Algorithms, Web Development",
                "Wednesday": "Math, Operating Systems, Machine Learning",
                "Thursday": "Data Structures, Computer Networks, AI",
                "Friday": "Physics, DBMS, Web Development"
            }
        }

    def get_response(self, query):
        query = query.lower()
        if "name" in query:
            return f"My name is {self.info['name']}."
        elif "college" in query:
            return f"I study at {self.info['college']}."
        elif "department" in query:
            return f"I am in the {self.info['department']} department."
        elif "year" in query:
            return f"I am in {self.info['year']}."
        elif "gpa" in query:
            return f"My current GPA is {self.info['gpa']}."
        elif "events" in query:
            events = ", ".join(self.info["upcoming_events"])
            return f"Upcoming events are: {events}."
        elif "timetable" in query or "schedule" in query:
            timetable = "\n".join([f"{day}: {subjects}" for day, subjects in self.info["timetable"].items()])
            return f"My timetable is:\n{timetable}"
        else:
            return "I'm sorry, I don't have information on that. Try asking about my college, department, GPA, events, or timetable."

# Example usage
bot = CollegeInfoBot()
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break
    response = bot.get_response(query)
    print("Bot:", response)


Q2


from heapq import heappush, heappop

# A helper function to find the position of the empty space (0) in the puzzle
def find_blank_position(state):
    return state.index(0)

# Helper function to generate new states from the current state
def generate_moves(state):
    blank = find_blank_position(state)
    moves = []
    
    # Define possible moves based on the position of the blank space
    if blank >= 3:  # Can move up
        moves.append(blank - 3)
    if blank < 6:   # Can move down
        moves.append(blank + 3)
    if blank % 3 > 0:  # Can move left
        moves.append(blank - 1)
    if blank % 3 < 2:  # Can move right
        moves.append(blank + 1)
    
    return moves

# Function to move the blank position and create a new state
def make_move(state, blank, target):
    new_state = state[:]
    new_state[blank], new_state[target] = new_state[target], new_state[blank]
    return new_state

# Heuristic function (Manhattan distance)
def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):
        current = state.index(i)
        target = goal.index(i)
        distance += abs(current // 3 - target // 3) + abs(current % 3 - target % 3)
    return distance

# A* search algorithm to solve the 8-puzzle
def solve_puzzle(initial, goal):
    # Priority queue for A* search
    open_set = []
    heappush(open_set, (0 + manhattan_distance(initial, goal), 0, initial, []))
    visited = set()
    
    while open_set:
        estimated_cost, g, current, path = heappop(open_set)
        
        # Check if goal state is reached
        if current == goal:
            return path + [current]
        
        visited.add(tuple(current))
        
        # Generate new states from valid moves
        blank = find_blank_position(current)
        for target in generate_moves(current):
            new_state = make_move(current, blank, target)
            new_path = path + [current]
            if tuple(new_state) not in visited:
                heappush(open_set, (g + 1 + manhattan_distance(new_state, goal), g + 1, new_state, new_path))
    
    return None

# Initial and goal states
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Solve the puzzle
solution = solve_puzzle(initial_state, goal_state)
if solution:
    print("Solution found:")
    for step in solution:
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print()
else:
    print("No solution exists.")
