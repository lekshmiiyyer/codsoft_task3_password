from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

import random
import string

def generate_password(length):
    # Define character sets for each category
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one character from each category
    password = (
        random.choice(uppercase_letters) +
        random.choice(lowercase_letters) +
        random.choice(digits) +
        random.choice(special_characters)
    )

    # Generate remaining characters randomly
    remaining_length = length - 4
    password += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))

    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    try:
        length = int(request.form['length'])
        password = generate_password(length)
        return render_template('index.html', password=password)
    except ValueError:
        return render_template('index.html', error="Please enter a valid length")

if __name__ == '__main__':
    app.run(debug=True)
