from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import sqlalchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite://'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')       

@app.route('/add')
def add():
    return render_template('add.html')       

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    entry = request.form['entry']
    author = request.form['author']
    datetimeEntry = datetime.now()
    
    data['post'].append({
        'id': 
        'title': title,
        'subtitle': subtitle,
        'entry': entry,
        'author': author,
        'datetime': datetimeEntry.strftime("%m/%d/%Y, %H:%M:%S")
    })

    with open('journal_entry.txt', 'w') as outfile:
        json.dump(data, outfile)

    return redirect(url_for('index'))         


if __name__ == '__main__':
    app.run(debug=True)  