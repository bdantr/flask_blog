from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from hashlib import md5

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), unique=True,index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password = db.Column(db.String(256))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about = db.Column(db.string(140))
    lastseen= db.Column(db.DateTime ,default=datetime.utcnow)




    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def avatar(self,size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        avatar = f'https://gravatar.com/avatar/{digest}?d=identicon&s={size}'
        return avatar


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    body = db.Column(db.String())
    published = db.Column(db.DateTime, index=True,default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))