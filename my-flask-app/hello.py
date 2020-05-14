from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)
    
""" 
@app.route('/user/<rc>') #kapag nagenter ka sa url may /user/rc
def show_user_profile(rc):
    return 'User RC'
"""

@app.route('/hello/')
@app.route('/hello/<name>')
def hello (name=None):
    return render_template('hello.html' , name=name)