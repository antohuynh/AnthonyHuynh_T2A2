from flask import Blueprint, request, abort
from init import db, bcrypt
from models.user import User, UserSchema
from datetime import date, timedelta
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix = '/auth')

# Register a new user
@auth_bp.route('/register/', methods=['POST'])
def auth_register():
    try:
        data = UserSchema().load(request.json)
        user = User(
            email = data['email'],
            password = bcrypt.generate_password_hash(data['password']).decode('utf-8'),
            name = data['name'],
            date_joined = date.today()
        )

        db.session.add(user)
        db.session.commit()
        return {'message': 'You have been registered!', 'user': UserSchema(exclude=['password']).dump(user)}, 201

    except IntegrityError:
        return {'Error': 'Email address has already been registered'}, 409

# Login a registered user
def auth_login():
    stmt = db.select(User).filter_by(email=request.json['email'])
    user = db.session.scalar(stmt)

    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity = str(user.id), expires_delta = timedelta(days=1))
        return {'message': 'You have logged in successfully!', 'email': user.email, 'token': token, 'is_admin': user.is_admin}

    else:
        return{'Error': 'Invalid email or password try again'}, 401

# Authorize a registered user
def authorize():
    stmt = db.select(User).filter_by(id = get_jwt_identity())
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)

    return True