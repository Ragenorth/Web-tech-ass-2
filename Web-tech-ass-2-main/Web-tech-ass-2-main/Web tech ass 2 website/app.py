from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('123.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    comment = request.form['comment']

    with open('feedback.txt', 'a') as file:
        file.write(f"Name: {name}\nEmail: {email}\nComment: {comment}\n\n")

    return 'Feedback submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True, port = 80)
