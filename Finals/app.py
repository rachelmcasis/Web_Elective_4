from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime
from tinydb import TinyDB, Query

app = Flask(__name__)

db = TinyDB('db.json')

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin@admin.app' or request.form['password'] != 'password123':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/index')
def index():
    all_post = db.all()
    return render_template('index.html', posts = all_post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = db.get(doc_id= post_id)
    return render_template('post.html', post= post)

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
    
    db.insert({
        'title': title,
        'subtitle': subtitle,
        'entry': entry,
        'author': author,
        'datetime': datetimeEntry.strftime("%B %d, %Y %I:%M %p")
    })
   
    return redirect(url_for('index'))     

@app.route('/update/<int:post_id>')
def update(post_id):
    post = db.get(doc_id= post_id)
    return render_template('update.html' , post=post)       


@app.route('/updatepost', methods=['POST'])
def updatepost():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        entry = request.form['entry']
        author = request.form['author']
        datetimeEntry = datetime.now()
        post_id = request.form['post_id']

        db.update({
            'title': title,
            'subtitle': subtitle,
            'entry': entry,
            'author': author,
            'datetime': datetimeEntry.strftime("%B %d, %Y %I:%M %p")
            }
            , doc_ids=[int(post_id)])
   
    return redirect(url_for('index'))         

@app.route('/delete/<int:post_id>')
def delete(post_id):
    db.remove(doc_ids=[post_id])
    return redirect(url_for('index'))   