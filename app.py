from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def roulette():
    result = None
    points = 0

    # Options for the game
    numbers = ["00", "10", "20", "30", "40", "50"]
    colors = ["赤", "黒"]
    bet_types = ["数字と色の組み合わせ", "数字のみ", "色のみ"]

    if request.method == 'POST':
        # Retrieve user selections
        selected_number = request.form.get('number')
        selected_color = request.form.get('color')
        bet_type = request.form.get('bet_type')

        # Computer's random selection
        computer_number = random.choice(numbers)
        computer_color = random.choice(colors)

        # Determine points based on the bet type
        if bet_type == "数字と色の組み合わせ":
            if selected_number == computer_number and selected_color == computer_color:
                points = 100
                result = f"あなたの選択: 数字({selected_number}) 色({selected_color}) 賭ける種類({bet_type})<br>コンピューターの選択: 数字({computer_number}) 色({computer_color})<br>結果: {points}点"
            else:
                result = f"あなたの選択: 数字({selected_number}) 色({selected_color}) 賭ける種類({bet_type})<br>コンピューターの選択: 数字({computer_number}) 色({computer_color})<br>結果: 0点"

        elif bet_type == "数字のみ":
            if selected_number == computer_number:
                points = 50
                result = f"あなたの選択: 数字({selected_number}) 賭ける種類({bet_type})<br>コンピューターの選択: 数字({computer_number})<br>結果: {points}点"
            else:
                result = f"あなたの選択: 数字({selected_number}) 賭ける種類({bet_type})<br>コンピューターの選択: 数字({computer_number})<br>結果: 0点"

        elif bet_type == "色のみ":
            if selected_color == computer_color:
                points = 20
                result = f"あなたの選択: 色({selected_color}) 賭ける種類({bet_type})<br>コンピューターの選択: 色({computer_color})<br>結果: {points}点"
            else:
                result = f"あなたの選択: 色({selected_color}) 賭ける種類({bet_type})<br>コンピューターの選択: 色({computer_color})<br>結果: 0点"

    return render_template('roulette.html', numbers=numbers, colors=colors, bet_types=bet_types, result=result)

if __name__ == '__main__':
    app.run(debug=True)
