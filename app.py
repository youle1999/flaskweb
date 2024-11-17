from flask import Flask, render_template, request

app = Flask(__name__)

# Define the color mapping based on selected colors
color_mapping = {
    frozenset(['red']): '赤',
    frozenset(['green']): '緑',
    frozenset(['blue']): '青',
    frozenset(['red', 'green']): '黄',
    frozenset(['red', 'blue']): 'マゼンタ',
    frozenset(['green', 'blue']): 'シアン',
    frozenset(['red', 'green', 'blue']): '白',
    frozenset([]): '黒'  # No selection
}

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_colors = set()
    created_color = '黒'  # Default color if no selection

    if request.method == 'POST':
        # Get selected colors from form
        selected_colors = set(request.form.getlist('colors'))
        created_color = color_mapping.get(frozenset(selected_colors), '黒')

    return render_template('index.html', selected_colors=selected_colors, created_color=created_color)

if __name__ == '__main__':
    app.run(debug=True)
