from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Process login form data here
    return redirect(url_for('home'))

@app.route('/create_account', methods=['POST'])
def create_account():
    # Process account creation form data here
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)