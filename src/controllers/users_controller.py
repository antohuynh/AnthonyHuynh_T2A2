from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, UserSchema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required

users_bp = Blueprint('users',__name__, url_prefix='/users')

# View user profile
@users_bp.route('/profile/')

@jwt_required()
def get_profile():
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)
    return UserSchema(exclude=['password']).dump(user)

# Update user profile
@users_bp.route('/profile/', methods=['PUT', 'PATCH'])

@jwt_required()
def update_profile():
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)
    data = UserSchema().load(request.json)
    if request.json.get('name'):
        user.name = data['name']
    if request.json.get('email'):
        user.email = data['email']
    if request.json.get('password'):
        user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    db.session.commit()
    return {
        'message': 'You have updated your details!',
        'user': UserSchema(exclude=['password']).dump(user)
    }