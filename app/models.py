from app import db, bcrypt, slugify

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(20), unique=True)


    def __init__(self, username, password):
        self.username = username
        self.password= bcrypt.generate_password_hash(password, 10)

    
    def get_auth_token(self):
        """
        Encode a secure token for cookie
        """
        data = [str(self.id), self.password]
        return login_serializer.dumps(data)
 



    def is_authenticated(self):
        return True

 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return (self.id)


    def __repr__(self):
        return '<User %r>' % self.username



class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    slug = db.Column(db.String(80), index=True)


    
    
    def __init__(self, title, body, slug ):
        self.title = title
        self.body = body
        self.slug = slugify(title)
