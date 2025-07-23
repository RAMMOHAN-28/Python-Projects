def chatbot():
    print("Hello! I am a simple chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You:").lower().strip()

        if user_input in ["hi","hello","hey"]:
            print("Bot: Hi there! How can I assist you today?")

        elif user_input in ["how are you","how are you doing"]:
            print("Bot: I'm chatbox, you friendly assistent.")

        elif user_input in ["what can you do","helpme"]:
            print("Bot: I can answer simple questions and chat with you!")

        elif user_input in ["thankyou","thanks"]:
            print("Bot: you'rer welcome!")

        elif user_input in ["bye","exit","quit"]:
            print("Bot Goodbye! Have a great day!")
        
        elif user_input in ["what is python"]:
            print("Python is a interpreted language")

        else:
            print("Bot: I'm sorry, i didn't understand that. can your repharase?")

chatbot()