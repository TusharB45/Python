# Simple Chatbot 

def chatbot(input_text, user_name, user_data):
    responses = {
        "hello": f"Hello, {user_name}! How may I assist you today?",
        "how are you": "I'm just a computer program, so I don't have feelings, but I'm here to help!",
        "what's your name": f"You can call me ChatBot, {user_name}. What's on your mind?",
        "bye": f"Goodbye, {user_name}! It's been a pleasure chatting with you. Feel free to return if you have more questions.",
        "food": f"Tell me more about your favorite food, {user_name}.",
        "animals": f"What's your favorite animal, {user_name}?",
        "feelings": "I'm here to chat with you! How are you feeling today?",
    }

    input_text = input_text.lower()

    if input_text in responses:
        return responses[input_text]
    elif "food" in input_text:
        user_data["food"] = input("You: ")
        return f"Great choice, {user_name}! You enjoy {user_data['food']}? That sounds delicious."
    elif "animals" in input_text:
        user_data["animal"] = input("You: ")
        return f"Interesting choice, {user_name}! {user_data['animal']} are fascinating creatures."
    elif "feelings" in input_text:
        return "I'm here to chat with you! How are you feeling today?"
    else:
        return "I'm not quite sure how to respond to that. Please feel free to ask me something else."

def main():
    print("ChatBot: Hello! I'm a simple chatbot. What's your name?")
    user_name = input("You: ")
    user_data = {"name": user_name}

    print(f"ChatBot: Nice to meet you, {user_name}!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print(f"ChatBot: Goodbye, {user_name}! It's been a pleasure chatting with you.")
            break
        response = chatbot(user_input, user_name, user_data)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
