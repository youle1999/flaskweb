from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate BMI and determine classification
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100  # Convert height from cm to meters
    bmi = round(weight_kg / (height_m ** 2), 2)  # Calculate BMI and round to 2 decimal places
    
    # Determine classification based on BMI
    if bmi < 16:
        judgment = "痩せすぎ"
    elif 16 <= bmi < 17:
        judgment = "痩せ"
    elif 17 <= bmi < 18.5:
        judgment = "痩せぎみ"
    elif 18.5 <= bmi < 25:
        judgment = "普通体重"
    elif 25 <= bmi < 30:
        judgment = "肥満 (前段階)"
    elif 30 <= bmi < 35:
        judgment = "肥満 (1度)"
    elif 35 <= bmi < 40:
        judgment = "肥満 (2度)"
    else:
        judgment = "肥満 (3度)"
    
    return bmi, judgment

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    judgment = None
    error = None

    if request.method == 'POST':
        try:
            height_cm = float(request.form['height_cm'])
            weight_kg = float(request.form['weight_kg'])
            
            if height_cm <= 0 or weight_kg <= 0:
                error = "身長と体重は正の数で入力してください。"
            else:
                bmi, judgment = calculate_bmi(height_cm, weight_kg)
        except ValueError:
            error = "有効な数値を入力してください。"

    return render_template('index.html', bmi=bmi, judgment=judgment, error=error)

if __name__ == '__main__':
    app.run(debug=True)
