from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET','POST'])
def grades_form():
    grade_status = None
    if request.method == 'POST':
        first_grade = int(request.form["first_grade"])
        second_grade = int(request.form["second_grade"])
        third_grade = int(request.form["third_grade"])
        assistance = int(request.form["assistance"])
        grade_average = ((first_grade + second_grade + third_grade) / 3) / 10
        if (grade_average >= 4 and assistance >= 75):
            grade_status = "APROBADO"
        else:
            grade_status = "REPROBADO"
        return render_template('ejercicio1.html', grade_status=grade_status, grade_average=grade_average)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET','POST'])
def names_form():
    longest_name = None
    longest_name_char = 0
    if request.method == 'POST':
        names = [request.form["first_name"], request.form["second_name"], request.form["third_name"]]
        for i in names:
            char = 0
            for j in i:
                char += 1
            if char > longest_name_char:
                longest_name = i
                longest_name_char = char
        return render_template('ejercicio2.html', longest_name=longest_name, longest_name_char=longest_name_char)
    return render_template('ejercicio2.html')

if __name__ == "__main__":
    app.run(debug=True)
