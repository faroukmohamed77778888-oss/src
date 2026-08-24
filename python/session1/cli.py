from get_fun import get_response

def main_bot():
    print("Chatbot: Hi Farouk! How can I assist you?")

    while True:
        user_input = input("User: ").lower()
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input == "goodbye":
            break