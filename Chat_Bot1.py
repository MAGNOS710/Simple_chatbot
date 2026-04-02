from datetime import datetime

def contains(terms , content):

    content = content.lower()
    match : list[bool] = []
    for term in terms:
        match.append(term in content)
    return any(match)


def response(text ):
    if contains(['hello', 'hi', 'hey'], text):
        return "Hello! How can I assist you today?"
    elif contains(['bye', 'goodbye', 'see you'], text):
        return "Goodbye! Have a great day!"
    elif contains(['how are you', 'how are you doing'], text):
        return "I'm just a bot, but I'm here to help you!"
    elif contains(['what time is it', 'current time'], text):
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"
while True:
        user_input = input("YOU: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        bot_response  = response(user_input)
        print(f"Chatbot: {bot_response}")
