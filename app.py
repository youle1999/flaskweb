from flask import Flask, render_template, request, jsonify
import random
from collections import Counter

app = Flask(__name__)

# Function to determine poker hand role
def determine_role(numbers):
    count = Counter(numbers)
    counts = sorted(count.values(), reverse=True)

    if counts == [4, 1]:
        return "フォーカード"  # Four of a Kind
    elif counts == [3, 2]:
        return "フルハウス"  # Full House
    elif counts == [3, 1, 1]:
        return "スリーカード"  # Three of a Kind
    elif counts == [2, 2, 1]:
        return "ツーペア"  # Two Pair
    elif counts == [2, 1, 1, 1]:
        return "ワンペア"  # One Pair
    else:
        return "ノーハンド"  # No Hand

@app.route("/")
def index():
    # Generate random initial cards
    initial_cards = [random.randint(1, 5) for _ in range(5)]
    return render_template("index.html", initial_cards=initial_cards)

@app.route("/flip_card", methods=["POST"])
def flip_card():
    # Generate random card value between 1 and 5
    card_value = random.randint(1, 5)
    return jsonify({"card_value": card_value})

@app.route("/determine_role", methods=["POST"])
def determine_poker_role():
    # Get the numbers sent from the frontend
    numbers = request.json.get("numbers")
    # Determine the poker role
    role = determine_role(numbers)
    return jsonify({"role": role})

if __name__ == "__main__":
    app.run(debug=True)
