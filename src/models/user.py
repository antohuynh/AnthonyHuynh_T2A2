from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Length

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_joined = db.Column(db.Date)
    is_admin = db.Column(db.Boolean, default=False)

    runs = db.relationship('Run', back_populates = 'user', cascade = 'all, delete')
    reviews = db.relationship('Review', back_populates = 'user', cascade = 'all, delete')

class UserSchema(ma.Schema):
    