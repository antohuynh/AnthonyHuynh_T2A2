from flask import Blueprint, request
from init import db
from models.run import Run, RunSchema
from models.review import Review, ReviewSchema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import and_
from controllers.auth_controller import authorize

runs_bp = Blueprint('runs', __name__, url_prefix='/runs')


# Retrieivng information on all runs
@runs_bp.route('/')
def all_runs():
    stmt = db.select(Run)
    runs = db.session.scalars(stmt)

    return RunSchema(many=True).dump(runs)

# Retreiving information on one run
@runs_bp.route('/<int:run_id>/')
def one_run(run_id):
    stmt = db.select(Run).filter_by(id=run_id)
    run = db.session.scalars(stmt)

    if run:
        return RunSchema().dump(run)
    else:
        return {'Error': f'Run not found with id {run_id}'}, 404

# Adding a run to the database
@runs_bp.route('/', methods = ['POST'])

@jwt_required()
def add_run():
    
    data = RunSchema().load(request.json)
    run = Run(
        location = data['location'],
        distance = data['distance_covered'],
        runtype = data['runtyp'],
        date_tracked = date.today(),
        rpe = data['rpe'],
        user_id = get_jwt_identity()
    )
    db.session.add(run)
    db.session.commit()
    return {'message': f'You have tracked your run!',
            'run': RunSchema().dump(run)}, 201

# Updating a run's details
@runs_bp.route('/<int:run_id>/', methods = ['PUT', 'PATCH'])

@jwt_required()
def update_run(run_id):
    stmt = db.select(run).filter_by(id = run_id)
    run = db.session.scalar(stmt)
    if not run:
        return {'error': f'Run not found with id {run_id}'}, 404
    if run.user_id == int(get_jwt_identity()) or authorize():
        data = RunSchema().load(request.json, partial = True)
        if request.json.get('location'):
            run.title = data['location']
        if request.json.get('distance'):
            run.distance= data['distance']
        if request.json.get('runtype'):
            run.runtype = data['runtype']
        if request.json.get('rpe'):
            run.rpe = data['rpe']
        db.session.commit()
        return {'message': f'You have updated the details of your run!',
                'run': RunSchema().dump(run)
        }

# Deleting a run from the database
@runs_bp.route('/<int:run_id>/', methods=['DELETE'])

@jwt_required()
def delete_one_run(run_id):
    stmt = db.select(Run).filter_by(id = run_id)
    run = db.session.scalar(stmt)
    if not run:
        return {'error': f'We could not find your run'}, 404
    if run.user_id == int(get_jwt_identity()) or authorize():
        db.session.delete(run)
        db.session.commit()
        return {'message': f'Run has been deleted successfully'}


# Retrieving all reviews

@runs_bp.route('/<int:run_id>/reviews/')
def all_reviews_on_run(run_id):
    stmt = db.select(Run).filter_by(id=run_id)
    run = db.session.scalar(stmt)
    if not run:
        return {'error': f'Run not found!'}, 404
    stmt = db.select(Review).filter_by(run_id=run_id)
    reviews = db.session.scalars(stmt)
    if not reviews:
        return {'message': f'No reviews found!'}, 404
    return ReviewSchema(many=True, exclude = ['run']).dump(reviews)

# Retrieving one review
@runs_bp.route('/review/<int:review_id>/')
def get_one_review(review_id):
    stmt = db.select(Review).filter_by(id = review_id)
    review = db.session.scalar(stmt)
    if not review:
        return {'error': f'Review not found'}, 404
    else:
        return ReviewSchema().dump(review)

# Adding a review for a run
@runs_bp.route('/<int:run_id>/reviews/', methods = ['POST'])

@jwt_required()
def create_review(run_id):
    stmt = db.select(Run).filter_by(id=run_id)
    run = db.session.scalar(stmt)
    if run:
        data = ReviewSchema().load(request.json)
        review = ReviewSchema(
            description = data['description'],
            date = date.today(),
            user_id = get_jwt_identity(),
            run = run
        )
        db.session.add(review)
        db.session.commit()
        return {'message': f'You have created a review for your run!',
                'review': ReviewSchema(exclude = ['run']).dump(review)}, 201
    else:
        return {'Error': f'Run not found!'}, 404

# Updating a review
@runs_bp.route('/review/<int:review_id>', methods = ['PUT', 'PATCH'])
@jwt_required()
def edit_review(review_id):
    stmt = db.select(review).filter_by(id = review_id)
    review = db.session.scalar(stmt)
    if not review:
        return {'Error': f'Review not found with id {review_id}'}, 404
    if review.user_id == int(get_jwt_identity()) or authorize():
        data = ReviewSchema().load(request.json)
        if request.json.get('description'):
            review.description = data['description']
        db.session.commit()
        return {'message': f'You have updated review with id {review.id}!',
                'review': ReviewSchema().dump(review)}

# Deleting a review
@runs_bp.route('/reviews/<int:review_id>/', methods = ['DELETE'])

@jwt_required()
def delete_review(review_id):
    stmt = db.select(Review).filter_by(id = review_id)
    review = db.session.scalar(stmt)
    if not review:
        return {'error': f'No review found with id {review_id}'}, 404
    if review.user_id == int(get_jwt_identity()) or authorize():
        db.session.delete(review)
        db.session.commit()
        return {'message': 'This review has been deleted.'}
