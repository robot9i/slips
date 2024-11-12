import math

# Define the Alpha-Beta Pruning function
def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case: leaf node
    if depth == 3:
        return values[node_index]
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(2):  # Two children for each node
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):  # Two children for each node
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return min_eval

# Driver code
if __name__ == "__main__":
    # Example tree with depth 3 (2^3 leaf nodes)
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    # Initial values for alpha and beta
    alpha = -math.inf
    beta = math.inf
    optimal_value = alpha_beta_pruning(0, 0, True, values, alpha, beta)
    print("The optimal value is:", optimal_value)




Q2.

# Simple chatbot program

def chatbot_response(user_input):
    # A dictionary of questions and responses
    responses = {
        "hi": "Hello! How can I assist you today?",
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but thank you for asking! How can I assist you?",
        "what's your name": "I am your friendly chatbot!",
        "help": "Sure! I am here to answer your questions. Please ask me anything.",
        "bye": "Goodbye! Have a great day!",
    }
    
    # Clean and process the user's input
    user_input = user_input.lower()
    
    # Check if the user's input is in the responses
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I don't understand. Could you rephrase your question?"

# Main program to interact with the chatbot
def chatbot():
    print("Chatbot: Hi! I am a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Check if the user wants to exit
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        # Get response from the chatbot
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
chatbot()
