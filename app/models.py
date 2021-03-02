from . import db
from datetime import datetime

class Pitches(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(255))
    pitch_title = db.Column(db.String(255))
    pitch = db.Column(db.String)
    time =  db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.INteger,db.ForeignKey('users.id'))    
    comments = db.relationship('Comments', backref='title',lazy = 'dynamic')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'    

class Comments(db.Model):
    