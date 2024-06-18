import nltk
from nltk.stem import LancasterStemmer
import numpy as np
import json
import random
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model

# Initialize stemmer
stemmer = LancasterStemmer()

# Load intents file
with open("dataset/intents.json") as file:
    data = json.load(file)

# Load pickled data
with open("model/data.pickle", "rb") as f:
    words, labels, training, output = pickle.load(f)

# Load trained model
model = load_model("model.tflearn")

# Function to prepare input for prediction
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)

# Function to chat with the bot
def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        # Get predictions from model
        results = model.predict(np.array([bag_of_words(inp, words)]))
        results_index = np.argmax(results)
        tag = labels[results_index]

        # Select a random response from intents file
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        print(random.choice(responses))

# Start chatting
chat()
