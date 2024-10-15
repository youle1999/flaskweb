from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    next_day = None
    if request.method == 'POST':
        input_date_str = request.form['date']
        # Convert string input to datetime object
        input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
        # Calculate the next day
        next_day = input_date + timedelta(days=1)
        next_day = next_day.strftime('%Y年%m月%d日')
    
    return render_template('index.html', next_day=next_day)

if __name__ == '__main__':
    app.run(debug=True)
