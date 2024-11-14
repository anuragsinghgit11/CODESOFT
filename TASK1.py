#CHATBOT WITH RULE-BASED
#Build a simple chatbot that responds to user inputs based on
#predefined rules. Use if-else statements or pattern matching
#techniques to identify user queries and provide appropriate
#responses. This will give you a basic understanding of natural
#language processing and conversation flow.

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    # How are you?
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How about you?"

    # Name inquiry
    elif "what is your name" in user_input:
        return "I'm a simple chatbot created to assist you."

    # Help request
    elif "help" in user_input:
        return "Sure! What do you need help with?"

    # Farewells
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    # Jokes
    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"

    # Weather inquiry
    elif "weather" in user_input:
        return "I can't check the weather, but I hope it's sunny where you are!"

    # Hobbies
    elif "hobbies" in user_input:
        return "I enjoy chatting with you! What about you? What are your hobbies?"

    # Favorite color
    elif "favorite color" in user_input:
        return "I don’t have a favorite color, but I think blue is nice! What’s yours?"

    # Food preferences
    elif "favorite food" in user_input:
        return "I don't eat, but pizza seems to be a popular choice! What about you?"

    # Catch-all response for unrecognized inputs
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

# Example of using the chatbot
def start_chat():
    print("Welcome to the Chatbot! Type 'bye' or 'goodbye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot:", chatbot_response(user_input))
            break
        else:
            print("Chatbot:", chatbot_response(user_input))

# Run the chatbot
if __name__ == "__main__":
    start_chat()
