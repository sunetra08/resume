from flask import Flask, request

app = Flask(__name__)


@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Here you can add code to save the form data to a file or a database
    # For example, you can write the data to a CSV file like this:
    with open('responses.csv', 'a') as f:
        f.write(f'{name},{email},{subject},{message}\n')

    return 'Form submitted successfully!'


if __name__ == '__main__':
    app.run(debug=True)
