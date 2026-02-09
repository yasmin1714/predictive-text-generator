import csv
import random
from collections import defaultdict, Counter

# Bigram Markov Model
bigram_model = defaultdict(Counter)

def preprocess(text):
    return text.lower().strip().split()

# Train from Twitter dataset
def train_from_csv(csv_path, limit=50000):
    with open(csv_path, encoding="latin-1") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i >= limit:
                break
            sentence = row[-1]
            words = preprocess(sentence)
            for j in range(len(words) - 1):
                bigram_model[words[j]][words[j + 1]] += 1

# Add a full sentence (context learning)
def add_user_sentence(sentence):
    words = preprocess(sentence)
    for i in range(len(words) - 1):
        bigram_model[words[i]][words[i + 1]] += 1

# ⭐ Add frequently used word (increase its weight)
def add_frequent_word(previous_word, frequent_word, boost=5):
    """
    boost increases probability of the frequent word
    """
    previous_word = previous_word.lower()
    frequent_word = frequent_word.lower()
    bigram_model[previous_word][frequent_word] += boost

# Predict next word
def predict_next_word(text):
    words = preprocess(text)
    if not words:
        return "No input"

    last_word = words[-1]

    if last_word in bigram_model:
        return random.choices(
            list(bigram_model[last_word].keys()),
            weights=bigram_model[last_word].values()
        )[0]

    return "No prediction"
def train_default_data():
    sentences = [
        "i love machine learning",
        "i love artificial intelligence",
        "machine learning is powerful",
        "artificial intelligence is the future",
        "i am learning ai",
        "streamlit makes apps easy",
        "natural language processing is interesting"
    ]
    for s in sentences:
        add_user_sentence(s)
