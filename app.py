from flask import Flask, render_template, request

app = Flask(__name__)


color_mapping = {
    frozenset(['red']): '赤',
    frozenset(['green']): '緑',
    frozenset(['blue']): '青',
    frozenset(['red', 'green']): '黄',
    frozenset(['red', 'blue']): 'マゼンタ',
    frozenset(['green', 'blue']): 'シアン',
    frozenset(['red', 'green', 'blue']): '白',
    frozenset([]): '黒⚫️'  
}

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_colors = set()
    created_color = 'Black'  

    if request.method == 'POST':
        selected_colors = set(request.form.getlist('colors'))
        created_color = color_mapping.get(frozenset(selected_colors), '黒')

    return render_template('index.html', selected_colors=selected_colors, created_color=created_color)

if __name__ == '__main__':
    app.run(debug=True)
