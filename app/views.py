from flask import render_template, flash, redirect, url_for, request, session,escape, abort, g
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from app import app, db, bcrypt

from .models import User, Post

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'


@app.route('/')
def index():
    session['key'] = 'value'
    return render_template('index.html', title="home")
    
    

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'] , request.form['password'] )
    username = request.form['username']
    password = request.form['password']
    storeduser = User.query.filter_by(username=username).first()
    if storeduser is not None and storeduser.username == request.form['username']:
        return 'User already Exist !'
    else:
        db.session.add(user)
        db.session.commit()
        session['username'] = username
        flash('User successfully registered')
        return redirect(url_for('index'))
    



@app.route('/login', methods=['GET','POST'])
def login():


    if g.user.is_authenticated:
        return redirect(url_for('index'))
    else:
        if request.method == 'GET':
            return render_template('login.html')

        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            session['logged_in'] = True
            flash('Logged in successfully')
            return redirect(request.args.get('next') or url_for('index'))
        else:    
            flash('Invalid Username or password')
            return redirect(url_for('login'))

       
       



@app.route('/logout')
def logout():
    logout_user()
    session.pop('logged_in', None)
    return redirect(url_for('index')) 



@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user

@app.route('/posts')
def posts():
       
        return render_template("posts.html", posts=Post.query.all())
    

    
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
        



@app.route('/posts/<title>')
@login_required
def show(title):
 
    link = db.session.query(Post).filter_by(title = title).one()
    return render_template("post.html", post=link, pid=id, link=title)
    
    
@app.route('/posts/delete/<int:id>')
@login_required
def delete(id):
    post = Post.query.get(id)
    if post is None:
        flash('Post not found.')
        return redirect(url_for('index'))
        
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted.')
    return redirect(url_for('index'))
    
    
@app.route('/posts/<title>/edit',  methods=['GET', 'POST'])
@login_required
def edit(title, body=None):

    kwargs = {'title': title, 'body' : body}

    link = db.session.query(Post).filter_by(title = title).one()


    if request.method == 'GET':
        return render_template("edit.html", postq=link, post=link)
    update = db.session.query(Post).filter_by(title=title).one()
    update.title =  request.form['title']
    update.body = request.form['body']

    db.session.add(update)
    db.session.commit()
    flash('Your post has been updated.')
    return redirect(url_for('index'))


    
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404