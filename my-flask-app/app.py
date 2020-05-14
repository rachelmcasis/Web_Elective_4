from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

# Route for handling the login page logic

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'test@flask.app' or request.form['password'] != 'password123':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('next'))
    return render_template('login.html', error=error)


@app.route('/home')
def next():
  return render_template('success.html')