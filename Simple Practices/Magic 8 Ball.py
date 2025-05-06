import random

while True:
    question = input("Ask a yes or no question (or type 'exit' to quit): ")
    if question.lower() == 'exit':
        print("Goodbye!")
        break
    responses = [
        "Yes, definitely.",
        "No, not at all.",
        "Ask again later.",
        "Absolutely!",
        "I wouldn't count on it.",
        "Yes, in due time.",
        "No way!",
        "It is certain.",
        "Don't hold your breath.",
        "Yes, but be careful."
    ]
    answer = random.choice(responses)
    print("Magic 8 Ball says:", answer)
    