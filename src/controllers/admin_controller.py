from flask import Blueprint, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db, bcrypt
from model.user import User, UserSchema