from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('123.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    department = request.form['department']
    address = request.form['address']
    dob = request.form['dob']
    gender = request.form['gender']
    comment = request.form['comment']

    with open('feedback.txt', 'a') as file:
        file.write(f"Name: {name}\nEmail: {email}\nPhone:{phone}\nDepartment:{department}\nAddress:{address}\nDate of birth: {dob}\nGender:{gender}\nComment: {comment}\n\n")

    return redirect(url_for('submitted'))

@app.route('/submitted')
def submitted():
    return render_template('submitted.html')

if __name__ == '__main__':
    app.run(debug=True, port=80)
