from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import recommend_food, mood_response, chatbot_reply, add_order, get_history

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "AI Backend Running 🚀"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user = data.get("user")
    query = data.get("query")

    return jsonify(recommend_food(user, query))

@app.route('/mood', methods=['POST'])
def mood():
    data = request.json
    user = data.get("user")
    mood = data.get("mood")

    return jsonify(mood_response(user, mood))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user = data.get("user")
    msg = data.get("message")

    return jsonify({"reply": chatbot_reply(user, msg)})

@app.route('/order', methods=['POST'])
def order():
    data = request.json
    user = data.get("user")
    food = data.get("food")

    add_order(user, food)
    return jsonify({"msg": "Order added"})

@app.route('/history', methods=['POST'])
def history():
    data = request.json
    user = data.get("user")

    return jsonify(get_history(user))

if __name__ == '__main__':
    app.run(debug=True)