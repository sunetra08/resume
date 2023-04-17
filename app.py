from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Define database connection and cursor
conn = sqlite3.connect('contact.db', check_same_thread=False)
c = conn.cursor()

# Create a table for the contact form responses
c.execute('''CREATE TABLE IF NOT EXISTS contacts
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              email TEXT,
              subject TEXT,
              message TEXT)''')
conn.commit()

@app.route('/')
def contact():
    return render_template('contact.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Insert the response into the database
    c.execute("INSERT INTO contacts (name, email, subject, message) VALUES (?, ?, ?, ?)",
              (name, email, subject, message))
    conn.commit()

    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
