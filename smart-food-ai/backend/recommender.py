from sentence_transformers import SentenceTransformer
import numpy as np
from data import foods
import random

model = SentenceTransformer('all-MiniLM-L6-v2')

food_vectors = model.encode([f["text"] for f in foods])

# 🔥 MEMORY
user_memory = {}
order_history = {}

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def store_user(user, vector):
    user_memory.setdefault(user, []).append(vector)

def get_user_pref(user):
    if user not in user_memory:
        return None
    return np.mean(user_memory[user], axis=0)

def recommend_food(user, query):
    q_vec = model.encode([query])[0]
    store_user(user, q_vec)

    pref = get_user_pref(user)
    scores = []

    for i, vec in enumerate(food_vectors):
        score = cosine_similarity(q_vec, vec)

        if pref is not None:
            score = 0.7*score + 0.3*cosine_similarity(pref, vec)

        scores.append((score, foods[i]))

    scores.sort(reverse=True, key=lambda x: x[0])
    return [f[1] for f in scores[:3]]

# 🔥 ORDER HISTORY
def add_order(user, food):
    order_history.setdefault(user, []).append(food)

def get_history(user):
    return order_history.get(user, [])

# 🔥 MOOD AI
def mood_response(user, mood):
    quotes = {
        "sad": ["You deserve something sweet 🍫", "Better days are coming ❤️"],
        "happy": ["Keep smiling 😄", "Celebrate with good food 🍕"],
        "stressed": ["Relax and recharge 🧘", "Take a break and eat well 🍲"]
    }

    foods = recommend_food(user, mood)

    coupon = f"DISCOUNT{random.randint(10,50)}%"

    return {
        "foods": foods,
        "quote": random.choice(quotes.get(mood, ["Enjoy your day!"])),
        "coupon": coupon
    }

# 🔥 CHATBOT
def chatbot_reply(user, message):
    message = message.lower()

    if "hungry" in message:
        rec = recommend_food(user, "food")
        return f"You should try {rec[0]['name']} 🍽️"

    if "sad" in message:
        return "Hey, don't worry ❤️ let's get something sweet!"

    return "Tell me your mood or food craving 😊"