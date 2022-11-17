from flask import Blueprint, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import authorize
from init import db, bcrypt
from models.user import User, UserSchema

admin_bp = Blueprint('admin', __name__, url_prefix = '/admin')

# Admins must be authenticated, only admins can give admin access
@admin_bp.route('/<int:user_id>/give_admin/', methods = ['POST'])

@jwt_required()
def give_admin(user_id):
    authorize()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    
    if user:
        if user.is_admin:
            return {'message': 'This user is already an admin!'}
        else:
            user.is_admin = True
            db.session.commit()
            return {'message': 'You have successfully given this user admin permissions.'}
    else:
        abort(404, description = f'User with id {user_id} does not exist!')


# Removing admin access from a user

@admin_bp.route('/<int:user_id>/remove_admin/', methods = ['POST'])

@jwt_required()
def remove_admin(user_id):
    authorize()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        if user.is_admin:
            user.is_admin = False
            db.session.commit()
            return {'message': 'You have successfully removed admin permissions from this user.'}
        else:
            return {'message': 'This user is not an admin!'}
    else:
        abort(404, description = f'The user with id {user_id} does not exist!')

#Retrieving list of all registered users

@admin_bp.route('/all_users/')

@jwt_required()
def all_users():
    authorize()
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude = ['password']).dump(users)

# Retrieving one registered user

@admin_bp.route('/user/<int:user_id>')

@jwt_required()
def one_user(user_id):
    authorize()
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude = ['password']).dump(user)
    else:
        abort(404, description = f'The user with id {user_id} does not exist!')

# Updating a user's information

@admin_bp.route('/user/<int:user_id>', methods=['PUT', 'PATCH'])

@jwt_required()
def update_user(user_id):
    authorize()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)

    if user:
        data = UserSchema().load(request.json)
        if request.json.get('name'):
            user.name = data['name']
        if request.json.get('email'):
            user.email = data['email']
        if request.json.get('password'):
            user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        db.session.commit()
        return {
            'message': "You have updated this user's details!",
            'user': UserSchema(exclude=['password']).dump(user)
        }
    else:
        abort(404, description = f'The user with id {user_id} does not exist!')        

# Deleting a registered user

@admin_bp.route('user/<int:user_id>', methods = ['DELETE'])

@jwt_required()
def delete_user(user_id):
    authorize()
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {
            'message': 'You have deleted this user successfully!.',
            'user_id': user_id,
            'name': user.name,
            'email': user.email
        }
    else:
        abort(404, description = f'The user with id {user_id} does not exist!')