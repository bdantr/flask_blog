from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), unique=True,index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password = db.Column(db.String(256))
    posts = db.relationship('Post', backref='author', lazy='dynamic')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    body = db.Column(db.String())
    published = db.Column(db.DateTime, index=True,default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))