from flask import Flask, render_template, request, url_for, flash, redirect
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'itsallsecret'

messages = [{'title': 'Message One', 'content': 'Message One Content', 'secret': 'secure', 'salt': '123456'},
            {'title': 'Message Two', 'content': 'Message Two Content', 'secret': '123456', 'salt': 'secure'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        secret = request.form['secret']
        
        title, content, secret, res = input_validation(title, content, secret)

        if res:
            hash, salt = hashnsalt(secret)
            messages.append({'title': title, 'content': content, 'secret': hash, 'salt': salt})
            return redirect(url_for('index'))
        else:
            flash("Bad form input!")

    return render_template('create.html')


def input_validation(title: str, content: str, secret: str) -> (str, str, str, bool):
    title = title.replace('>', '&gt;').replace('<', '&lt;')
    content = content.replace('>', '&gt;').replace('<', '&lt;')
    secret = secret.replace('>', '&gt;').replace('<', '&lt;')

    res = True if (title and content and secret) else False

    return (title, content, secret, res)

    
def hashnsalt(secret):
    # Generate a random salt (a string of random characters)
    salt = bcrypt.gensalt()
    
    # Hash the password using the generated salt
    hashed_password = bcrypt.hashpw(secret.encode('utf-8'), salt)
    
    return (hashed_password, salt)
