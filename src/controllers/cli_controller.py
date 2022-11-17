from init import db, bcrypt
from flask import Blueprint
from models.run import Run 
from models.user import User 
from models.review import Review
from datetime import date

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            email = 'admin@runningrunning.com',
            password = bcrypt.generate_password_hash('password123').decode('utf-8'),
            is_admin = True
        ),
        User(
            name = 'John Doe',
            email = 'johndoe@alphamail.com',
            password = bcrypt.generate_password_hash('john123').decode('utf-8'),
            date_joined = '01/01/2022'
        ),
        User(
            name = 'Jane Doe',
            email = 'janedoe@alphamail.com',
            password = bcrypt.generate_password_hash('jane123').decode('utf-8'),
            date_joined = '01/01/2021'
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    runs = [
        Run(
            location = 'Strathfield',
            distance = '5',
            runtype = 'Easy',
            date_tracked = date.today(),
            rpe = '6',
            user_id = users[2].id
        ),
        Run(
            location = 'Hurstville',
            distance = '20',
            runtype = 'Long',
            date_tracked = date.today(),
            rpe = '10',
            user_id = users[1].id
        ),
        Run(
            location = 'Berala',
            distance = '7',
            runtype = 'Tempo',
            date_tracked = date.today(),
            rpe = '8',
            user_id = users[2].id
        )

    ]

    db.session.add_all(runs)
    db.session.commit()

    reviews = [
        Review(
            description = 'Set a PB for this distance!',
            user = users[2],
            run = runs[0],
            date = date.today(),
        ),

        Review(
            description = 'Was sick for the whole week and really struggled',
            user = users[1],
            run = runs[1],
            date = date.today(),
        ),

        Review(
            description = 'Breezed through the session',
            user = users[2],
            run = runs[2],
            date = date.today(),
        )

        
    ]

    db.session.add_all(reviews)
    db.session.commit()
    print("Table seeded")