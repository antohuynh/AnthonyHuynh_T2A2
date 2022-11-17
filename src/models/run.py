from init import db, ma 
from marshmallow import fields
from marshmallow.validate import OneOf, Length

VALID_RUNTYPE = ('Easy', 'Recovery', 'Tempo', 'Speed', 'Long Run')

class Run(db.model):

    __tablename__ ='runs'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    distance = db.Column(db.Integer)
    runtype = db.Column(db.String)
    date_tracked = db.Column(db.Date)
    rpe = db.Column(db.integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates = 'runs')
    reviews = db.relationship('Review', back_populates = 'runs', cascade = 'all, delete')

class RunSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    reviews = fields.List(fields.Nested('ReviewSchema', exclude = ['run']))


    runtype = fields.String(validate=OneOf(VALID_RUNTYPE, error=f'Only these specific runtypes are allowed: {VALID_RUNTYPE}'))

    class Meta:
        fields = ('id', 'location', 'distance', 'runtype', 'date_tracked', 'rpe', 'user', 'reviews')
        ordered = True