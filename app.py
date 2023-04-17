from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'responses.db'

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Save the response to the database
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS responses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, subject TEXT, message TEXT)')
        cursor.execute('INSERT INTO responses (name, email, subject, message) VALUES (?, ?, ?, ?)', (name, email, subject, message))
        conn.commit()

    return 'Thank you for your message!'

if __
