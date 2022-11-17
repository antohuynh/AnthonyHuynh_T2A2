from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Length

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(750), nullable=False)
    date = db.Column(db.Date)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    run_id = db.Column(db.Integer, db.ForeignKey('runs.id'), nullable=False)

    user = db.relationship('User', back_populates= 'reviews')
    run = db.relationship('Run', back_populates= 'reviews')

class ReviewSchema(ma.Schema):

    user = fields.Nested('UserSchema', only = ['name', 'email'])
    run = fields.Nested('RunSchema', only = ['location', 'runtype'])

    description = fields.String(required=True, validate=Length(min=1))

    class Meta:
        fields = ('id', 'description', 'date', 'run', 'user')
        ordered = True
  