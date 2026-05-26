import random

def ai_chatbot():
    print("Hello, I am an AI Chatbot 👋 How can I help you today?")
    
    goodbyes = ["Goodbye! 👋", "See you later!", "Bye! Have a great day! 😎"]
    greetings = ["Hello! 👋", "Hi there! 😊", "Hey! How are you doing today? 😎"]
    thanks = ["You're welcome! 😊", "No problem! 😎", "My pleasure! 😄"]
    
    # We can add additional user inputs here for the program to understand
    responses = {
        "hello": greetings,
        "hi": greetings,
        "hey": greetings,
        "greetings": greetings,
        "thanks": thanks,
        "thank you": thanks,
        "ty": thanks,
        "exit": goodbyes,
        "quit": goodbyes,
        "bye": goodbyes,
        "byebye": goodbyes,
        "goodbye": goodbyes,
        "good bye": goodbyes
    }
    
    default_responses = [
        "I'm not sure I understand 😟", 
        "Could you please rephrase that? 🤔", 
        "I'm still learning, can you explain? 😅"
    ]

    while True:
        user_input = input("You: ").lower().strip()
        
        reply = responses.get(user_input)
        
        # Here we used random.choice so the program gives a different reply everytime user asks the same question

        if reply is not None:
            print(f"AI: {random.choice(reply)}")
            
            if user_input in ("exit", "quit", "bye", "goodbye"):
                break

        else:
            print(f"AI: {random.choice(default_responses)}")

if __name__ == "__main__":
    ai_chatbot()