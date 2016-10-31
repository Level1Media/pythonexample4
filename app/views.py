from flask import render_template, flash, redirect, url_for, request, session, abort ,g
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from app import app, db
from .models import User, Post

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'


@app.route('/')
def index():
	return render_template('index.html', title="home")


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'] , request.form['password'] )
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('index'))


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index')) 



@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user

@app.route('/posts')
def posts():
 
    return render_template('/posts.html')
    
    
@app.route('/posts/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'GET':
         return render_template('create_post.html')
    else:
        title = request.form['title']
        body = request.form['body']
        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts'))

    
    