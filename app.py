from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Zodiac sign data
zodiac_signs = [
    ("山羊座", (12, 22), (1, 19)),
    ("水瓶座", (1, 20), (2, 18)),
    ("魚座", (2, 19), (3, 20)),
    ("牡羊座", (3, 21), (4, 19)),
    ("牡牛座", (4, 20), (5, 20)),
    ("双子座", (5, 21), (6, 21)),
    ("蟹座", (6, 22), (7, 22)),
    ("獅子座", (7, 23), (8, 22)),
    ("乙女座", (8, 23), (9, 22)),
    ("天秤座", (9, 23), (10, 23)),
    ("蠍座", (10, 24), (11, 21)),
    ("射手座", (11, 22), (12, 21))
]

# Function to find the zodiac sign based on birth month and day
def get_zodiac_sign(month, day):
    for sign, start, end in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return None

# Function to validate and adjust the date
def validate_date(month, day):
    try:
        # Try to create a valid date
        datetime(2024, month, day)  # Using a leap year for February 29
        return month, day  # If no exception, the date is valid
    except ValueError:
        # Adjust only invalid dates
        if month == 12:
            return 1, 1  # If December 32, move to January 1
        else:
            return month + 1, 1  # Move to the first day of the next month

@app.route('/', methods=['GET', 'POST'])
def index():
    zodiac = None
    selected_date = None
    if request.method == 'POST':
        month = int(request.form['month'])
        day = int(request.form['day'])

        # Validate and adjust the date if necessary
        month, day = validate_date(month, day)

        # Get the zodiac sign after validation
        zodiac = get_zodiac_sign(month, day)

        # Store the selected date for display
        selected_date = f"{month}月{day}日"

    return render_template('zodiac.html', zodiac=zodiac, selected_date=selected_date)

if __name__ == '__main__':
    app.run(debug=True)
