from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary to map genetic combinations to possible blood types for the child
blood_type_combinations = {
    ('AA', 'AA'): 'A型',
    ('AA', 'AO'): 'A型',
    ('AA', 'BB'): 'AB型',
    ('AA', 'BO'): 'A型, AB型',
    ('AA', 'OO'): 'A型',
    ('AA', 'AB'): 'A型, AB型',
    ('AO', 'AA'): 'A型',
    ('AO', 'AO'): 'A型, O型',
    ('AO', 'BB'): 'AB型',
    ('AO', 'BO'): 'A型, B型, AB型, O型',
    ('AO', 'OO'): 'A型, O型',
    ('AO', 'AB'): 'A型, AB型, B型',
    ('BB', 'AA'): 'AB型',
    ('BB', 'AO'): 'A型, AB型',
    ('BB', 'BB'): 'B型',
    ('BB', 'BO'): 'B型',
    ('BB', 'OO'): 'B型',
    ('BB', 'AB'): 'B型, AB型',
    ('BO', 'AA'): 'A型, AB型',
    ('BO', 'AO'): 'A型, B型, AB型, O型',
    ('BO', 'BB'): 'B型',
    ('BO', 'BO'): 'B型, O型',
    ('BO', 'OO'): 'B型, O型',
    ('BO', 'AB'): 'A型, B型, AB型, O型',
    ('OO', 'AA'): 'A型',
    ('OO', 'AO'): 'A型, O型',
    ('OO', 'BB'): 'B型',
    ('OO', 'BO'): 'B型, O型',
    ('OO', 'OO'): 'O型',
    ('OO', 'AB'): 'A型, B型',
    ('AB', 'AA'): 'A型, AB型',
    ('AB', 'AO'): 'A型, AB型, B型',
    ('AB', 'BB'): 'B型, AB型',
    ('AB', 'BO'): 'A型, B型, AB型, O型',
    ('AB', 'OO'): 'A型, B型',
    ('AB', 'AB'): 'A型, B型, AB型'
}

@app.route('/', methods=['GET', 'POST'])
def blood_type():
    result = None
    if request.method == 'POST':
        mother_genotype = request.form.get('mother_genotype')
        father_genotype = request.form.get('father_genotype')
        result = blood_type_combinations.get((mother_genotype, father_genotype), "不明")
    return render_template('blood_type.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
