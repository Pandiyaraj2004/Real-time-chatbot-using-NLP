import random
import nltk  # pip install nltk
from nltk.stem import PorterStemmer
from data import data  # Make sure the data file includes all updated intents
import json
# Initialize NLTK
nltk.download("punkt_tab")
stemmer = PorterStemmer()

with open("chatbot_data.json", "r", encoding="utf-8") as file:
    chat_data = json.load(file)

# Map intent categories to their corresponding response categories
INTENT_RESPONSE_MAP = {
    "greetings": "responses",
    "farewells": "farewell_responses",
    "questions": "question_responses",
    "small_talk": "small_talk_responses",
    "time": "time_responses",
    "date": "date_responses",
    "thanks": "thanks_responses",
    "emotions": "emotions_responses",
    "help": "help_responses",
    "food": "food_responses",
    "compliments": "compliments_responses",
    "weather": "weather_responses",
    "shopping": "shopping_responses",
    "health": "health_responses",
    "productivity": "productivity_responses",
    "fun": "fun_responses",
    "sleep": "sleep_responses",
    "travel": "travel_responses"
}


def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return [stemmer.stem(token) for token in tokens]


def get_response(user_input):
    processed_input = preprocess(user_input)

    for intent_category, response_category in INTENT_RESPONSE_MAP.items():
        for pattern in data[intent_category]:
            processed_pattern = preprocess(pattern)
            if all(word in processed_input for word in processed_pattern):
                return random.choice(data[response_category])

    for pair in chat_data:
        processed_pattern = preprocess(pair["input"])
        if all(word in processed_input for word in processed_pattern):
            return pair["response"]

    # Fallback for unknown inputs
    return "I'm not sure how to respond to that. Could you rephrase that?"


def chat():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")


# Main
if __name__ == "__main__":
    chat()
