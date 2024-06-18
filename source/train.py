import nltk
from nltk.stem import LancasterStemmer
import numpy as np
import json
import pickle
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Initialize stemmer
stemmer = LancasterStemmer()

# Load intents file
with open("dataset/intents.json") as file:
    data = json.load(file)

# Initialize lists
words = []
labels = []
docs_x = []
docs_y = []

# Tokenize words and create training data
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

# Stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

# Sort labels
labels = sorted(labels)

# Create training and output data
training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

# Convert to numpy arrays
training = np.array(training)
output = np.array(output)

# Save data to pickle files
with open("model/data.pickle", "wb") as f:
    pickle.dump((words, labels, training, output), f)

# Define Keras model
model = Sequential([
    Dense(8, input_shape=(len(training[0]),), activation='relu'),
    Dense(8, activation='relu'),
    Dense(len(output[0]), activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(training, output, epochs=1000, batch_size=8, verbose=1)

# Save model weights
model.save("model.tflearn")

print("Training is complete.")
