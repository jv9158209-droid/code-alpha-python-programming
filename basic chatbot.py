# ============================================================
# CODEALPHA - BASIC CHATBOT
# ============================================================


# ============================================================
# CHATBOT FUNCTION
# ============================================================

def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    # Greeting
    if user_input in ["hello", "hi", "hey"]:
        return "Hi! Nice to meet you!"

    # How are you
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How can I help you?"

    # Name
    elif user_input in ["what is your name", "what is your name?"]:
        return "My name is CodeAlpha Bot."

    # Help
    elif user_input in ["help", "help me"]:
        return "Sure! You can say hello, ask how I am, ask my name, or say bye."

    # Thank you
    elif user_input in ["thank you", "thanks"]:
        return "You're welcome!"

    # Goodbye
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day!"

    # Unknown message
    else:
        return "Sorry, I don't understand that."


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 50)
    print("             CODEALPHA BASIC CHATBOT")
    print("=" * 50)

    print("\nBot: Hello! I'm CodeAlpha Bot.")
    print("Bot: Type 'bye' to exit the chatbot.")

    while True:

        user_input = input("\nYou: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        # Stop chatbot when user says bye
        if user_input.lower().strip() in [
            "bye",
            "goodbye",
            "exit"
        ]:
            break

    print("\nChatbot closed.")
    print("Thank you for using CodeAlpha Basic Chatbot!")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()