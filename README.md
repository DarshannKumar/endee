# Smart Food AI – Personalized Recommendation Assistant 

An AI-powered food recommendation system built using vector embeddings, personalization, and conversational AI. This project simulates a real-world intelligent recommendation engine with mood-based suggestions, chatbot interaction, and dynamic coupon generation.

---

#  Problem Statement

Modern recommendation systems often fail to provide **personalized, context-aware suggestions**. Traditional systems:

- Do not understand user intent semantically  
- Ignore user history and behavior  
- Cannot adapt to emotions or mood  
- Lack conversational interaction  

As a result, users receive generic and irrelevant recommendations.

---

# 💡 Solution

This project implements an **AI-driven personalized recommendation system** that:

- Converts user queries into dense vector embeddings  
- Performs semantic similarity search on food items  
- Maintains user memory for personalization  
- Adapts recommendations based on mood and past behavior  
- Provides an interactive chatbot experience  
- Generates dynamic coupons based on user activity  

---

#  System Architecture

User Input (Query / Mood / Chat)
↓
Sentence Transformer (all-MiniLM-L6-v2)
↓ [Dense Vector Embedding]
Vector Similarity Engine (Cosine Similarity)
↓
User Memory (Past Queries & Preferences)
↓
Personalized Ranking Engine
↓
Food Recommendations + Coupons + Quotes
↓
Frontend UI (HTML/CSS/JS)


---

# ⚙️ How It Works

### 1. Embedding Generation
- Converts text queries into **384-dimensional dense vectors** using Sentence Transformers

### 2. Semantic Search
- Uses cosine similarity to find closest matching food items

### 3. Personalization (Key Feature)
- Stores user query vectors
- Computes average preference vector
- Combines:
  - 70% current query
  - 30% past behavior

### 4. Mood-Based Intelligence
- Detects user mood
- Suggests:
  - Relevant food
  - Motivational quotes
  - Discount coupons

### 5. Chatbot Interaction
- Handles natural language queries
- Provides conversational recommendations

### 6. Order History Tracking
- Stores user orders
- Influences future recommendations

---

# 🔥 Features

✅ Semantic search using vector embeddings  
✅ Personalized recommendations (memory-based)  
✅ Mood-aware suggestions with quotes  
✅ Dynamic coupon generation 🎟️  
✅ AI chatbot interaction 💬  
✅ Order history tracking 📜  
✅ Full-stack application (Flask + JS frontend)  
✅ Scalable to FAISS / vector databases  

---

# 🧪 Example Flow
User: "I feel sad"
↓
System:
Quote: "Better days are coming ❤️"
Coupon: DISCOUNT30%
Suggestion: Chocolate Cake 🍫


---

# 🛠️ Tech Stack

| Layer            | Technology |
|------------------|-----------|
| Backend API      | Flask |
| AI Model         | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Search    | Cosine Similarity (Upgradeable to FAISS) |
| Frontend         | HTML, CSS, JavaScript |
| Language         | Python 3 |

---

---

# 🛠️ Tech Stack

| Layer            | Technology |
|------------------|-----------|
| Backend API      | Flask |
| AI Model         | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Search    | Cosine Similarity (Upgradeable to FAISS) |
| Frontend         | HTML, CSS, JavaScript |
| Language         | Python 3 |

---


# 🚀 Setup & Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
2. Run Backend
cd backend
python app.py

Backend runs at:

http://127.0.0.1:5000
3. Run Frontend

Open:

frontend/index.html
🔗 API Reference
POST /recommend

Get personalized food recommendations

{
  "user": "darshan",
  "query": "pizza"
}
POST /mood

Get mood-based suggestions

{
  "user": "darshan",
  "mood": "sad"
}
POST /chat

Chat with AI

{
  "user": "darshan",
  "message": "I am hungry"
}
POST /order

Store order

{
  "user": "darshan",
  "food": "Pizza"
}
POST /history

Get user order history

{
  "user": "darshan"
}


