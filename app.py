from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        total_amount = int(request.form['total_amount'])
        num_people = int(request.form['num_people'])
        rounding_option = request.form['rounding_option']

        if total_amount < 200 or num_people < 2:
            return jsonify({'error': '支払総額は最低200円、人数は2人以上で入力してください。'}), 400

        # Calculate the base amount per person
        base_amount = total_amount // num_people

        result = []

        if rounding_option == "more_pays":
            # Round down to the nearest hundred
            base_amount = (base_amount // 100) * 100
            # Calculate total paid by (num_people - 1) participants
            subtotal = base_amount * (num_people - 1)
            # Last person pays the remaining amount
            last_person_amount = total_amount - subtotal

            # Fill the result list
            result = [base_amount] * (num_people - 1) + [last_person_amount]

        elif rounding_option == "less_pays":
            # Round up to the nearest hundred
            base_amount = ((base_amount + 99) // 100) * 100
            # Calculate total paid by (num_people - 1) participants
            subtotal = base_amount * (num_people - 1)
            # Last person pays the remaining amount
            last_person_amount = total_amount - subtotal

            # Fill the result list
            result = [base_amount] * (num_people - 1) + [last_person_amount]

        return jsonify({'result': result})

    except ValueError:
        return jsonify({'error': '有効な数値を入力してください。'}), 400

if __name__ == '__main__':
    app.run(debug=True)
