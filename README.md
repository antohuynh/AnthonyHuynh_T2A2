# Anthony Huynh - T2A2

---

## Link to GitHub Repository

### [GitHub Repo](https://github.com/antohuynh/AnthonyHuynh_T2A2)

## Table of Contents

[**How to Install**](#installation-instructions)

[**(R1) Identification of the problem you are trying to solve by building this particular app.**](#r1)

[**(R2) Why is it a problem that needs solving?**](#r2)

[**(R3) Why have you chosen this database system. What are the drawbacks compared to others?**](#r3)

[**(R4) Identify and discuss the key functionalities and benefits of an ORM**](#r4)

[**(R5) Document all endpoints for your API**](#r5)

[**(R6) An ERD for your app**](#r6)

[**(R7) Detail any third party services that your app will use***](#r7)

[**(R8) Describe your projects models in terms of the relationships they have with each other**](#r8)

[**(R9) Discuss the database relations to be implemented in your application**](#r9)

[**(R10) Describe the way tasks are allocated and tracked in your project**](#r10)

[**References**](#references)

---

## Installation Instructions

---

1. Open the terminal and create a new directory

2. Move into the directory and clone this repository using the following command:

   ```git clone https://github.com/antohuynh/AnthonyHuynh_T2A2```

3. Move into the src folder and activate a virtual environment using the following commands:

    ```python3 -m venv .venv```

    ```source .venv/bin/activate```

4. Install the required dependencies using the following command:

   ```pip install -r requirements.txt```

5. Open PostgreSQL in your terminal and create a new database named 'runninglog', a user with all access to this database, and set a password for this user

6. Open the .env.sample file and add the details above to the DATABASE_URL using the following template, replacing {user_name} and {password} with the ones set in step 5:

    ```DATABASE_URL = postgresql+psycopg2://{user_name}:{password}@127.0.0.1:5432/runninglog```

7. In the .env.sample file, set the JWT_SECRET_KEY to any word or string

8. Rename the .env.sample file to .env

9. Open the .flaskenv file, and set FLASK_RUN_PORT to any port that is available on your device

10. In the terminal, run the following command to create and seed tables in the database for testing purposes:

    ```flask db drop && flask db create && flask db seed```

11. In the terminal, run the following command to initialize the API webserver:

    ```flask run```

---

## (R1)

---
The purpose of this API Webserver is to provide users with a platform to record their runs and monitor/track their progress efficiently. The key problem addressed by this program is that of the inefficency of training logs and journals. This proves to be quite an issue for people who have been running for a long time and have hundreds if not thousands of runs logged. The API webserver allows users to access every run that they've ever tracked in a quick and efficient manner.

The application serves as a central log for which users can record their runs, add reviews as well as reflect on the the progress they have made. Specifics such as location of the run, distance covered, the type of run and rate of perceived exertion(rpe) are logged in order to provide a detailed analysis as well as a quantitative way of monitoring progress.This application dispels the need for manual hand-written training logs and does so in an efficient and effective manner.

---

## (R2)

---
For runners both experienced and inexperienced the ability to monitor your progress is crucial in ultimately achieving any athletic goal. Whilst the use of a handwritten log may be sufficient at first, the overwhelming amount of data which comes with progress monitoring can render any efficient training log useless, buried beneath pages and pages of recorded runs. The API webserver aims to remove the need for paper training logs whilst also providing users with a quick solution when it comes to accessing date on specific runs.

---

## (R3)

---
This project utilises PostgreSQL, a relational database management system which supports both SQL and JSON querying. PostgreSQL was chosen because it is highly extensible allowing for many additional features to be added improving levels of flexibility and freedom when it come to high level queries within the database. PostgreSQL is also open source meaning that a helpful and dedicated community are constantly maintaining its security and reliability. PostgreSQL, however, is not without its drawbacks. PostgreSQL has a comparatively low reading speed when compared to other DBMS such as MySQL. By default, PostgreSQL is also not available on all hosts, requiring installation which may lead to issues or problems depending on the user. Despite this however, PostgreSQL still proved to be the most suitable DBMS for this project.

---

## (R4)

---

An object-relational mapper provides an object-oriented layer between relational databases and object-oriented programming languages without having to write SQL queries. It standardizes interfaces reducing boilerplate and speeding development time.

In this particular project, an SQL query can be performed to retrieve all records from the Runs table with run id is 1

```sql
SELECT * FROM RUNS
WHERE run_id = 1
```

With the use of SQLAlchemy, an example of an object-relational mapper, we can recreate the exact same query within the databse:

```python
stmt = db.select(Run).filter_by(id=1)
run = db.session.scalar(stmt)
```

---

## (R5)

---

[Documentation of API Endpoints](docs/endpoints.md)

---

## (R6)

---

![ERD](docs/ERD.PNG)

---

## (R7)

---

This projects utilises the following third party services and PyPI packages:

- Flask-SQLAlchemy
  
  - SQLAlchemy is an SQL tookit and ORM written in Python that allows users to convert data from a relational database to Python objects. Flask-SQLAlchemy is an extension of Flask that provides support for SQLAlchemy in a Flask application. Flask-SQLAlchemy is used in this project to map tables from the database to a Python class object model, which can then be used to create, read, update and delete tables in the database.

- Flask

  - Flask is a web microframework that is used to create and develop web applications in Python. Flask allows users to easily build a simple web application in a single Python file, and does not require a specific directory structure, hence it is highly extensible. Flask is used in this project to set up the framework of the web application, and create routes that can receive web requests and send responses.

- Marshmallow

  - Marshmallow is an ORM library that allows the conversion of complex datatypes and objects to and from Python datatypes. Marshmallow can also be used to validate input data. Flask-Marshmallow is an extension to Flask that integrates Marshmallow with the Flask microframework. In this project, Marshmallow is used to transform JSON inputs into Python objects, as well as converting Python objects into valid JSON outputs. It is also used for data validation, where certain input fields must conform to a specified constraint.

- Bcrypt

  - Bcrypt is a password-hashing function that is used to encrypt passwords before it is stored in the database. A password string is hashed, meaning it is passed through an algorithm to map it to an encrypted string. A fixed length random value known as a salt is added to each hash in order to create a unique hash for every password. This unique salt value is used to decrypt the password hashes stored within the database for the purposes of authentication. Flask-Bcrypt is an extension to Flask that incorporates the Bcrypt function within a web application. For this project, Flask-Bcrypt is used primarily for the purposes of password encryption and user authentication.

- Flask-JWT-Extended

  - Flask-JWT-Extended is a Flask extension that provides support to Flask for using JWT tokens in order to protect routes in the framework. A JWT token is generated upon user login, and is included with every subsequent request made by the user to the server in order to authenticate their identity. This can also be used for the purposes of authorization, such as verifying administrator privileges before the web application returns a response to a request. For this project, Flask-JWT-Extended is used to protect routes by ensuring that the user must be logged in to make certain requests, as well as verifying administrator privileges in order to access admin-only routes.

- psycopg2

  - Psycopg is a PostgreSQL database adapter for the Python programming language. It is widely used in multi-threaded applications that handles a large number of create and delete operations, and concurrent insert or update operations to a PostgreSQL database. For this project, Psycopg was used to connect the Flask application to the PostgreSQL database, in order for the application to perform queries and operations on the database.

- Python-dotenv

  - Python-dotenv is a Python package that loads environment variables from a .env file into a Python module. For this project, Python-dotenv was used to retrieve values from a .flaskenv and .env file in order to configure the application. Variables are loaded from the .flaskenv file in order to configure the Flask application by specifying the Python file to run, activate the debugger and specify the server port the application will be running on. For sensitive information such as the database URL and the JWT secret key, the variables are loaded from the .env file.

---

## (R8)

---

There are 3 entities which are represented in this application. These 3 entities are the User model, Run model and Review model.

### **User Model**

The user model is used to represent users who have been registered in the database. As users can exist without having any runs recorded or reviews written, they do not require a foreign key. The two other models reference the User model through the use of foreign keys. There is a one to many relationship between the User model and both the Run model and Review model.

The code below demonstrates the relationship between the User model and the other two models. It is referenced by the other two models in their respective foreign key attributes. The db.relationship() function enables a bidirectional relationship in which the back_populates parameter connects both models together. The cascade parameter deletes all related runs and reviews to a user should the user be removed.

```python
runs = db.relationship('Run', back_populates = 'user', cascade = 'all, delete')
reviews = db.relationship('Review', back_populates = 'user', cascade = 'all, delete')
```

### **Run Model**

The Run model represents the runs that a user has added to the database to record. Each user can add many runs to the database, however each run that is added to the log can only be designated to one user. This is a one-to-many relationship that is represented in the following code snippet:

```python
user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

user = db.relationship('User', back_populates='runs')
```

The Run model is also referenced by the foreign key attributes within the Review model. Similarly to the User model, the relationship is established through the following line:

```python
reviews = db.relationship('Review', back_populates='run', cascade = 'all, delete')
```

### **Review Model**

The Review model represents the review that a user can add to their recorded runs. As such, reviews have a many-to-one relationship with both a user and a run, and have foreign keys that reference the User model and Game model.

```python
user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
game_id = db.Column(db.Integer, db.ForeignKey('runs.id'), nullable = False)

user = db.relationship('User', back_populates='reviews')
game = db.relationship('Review', back_populates='reviews')
```

---

## (R9)

---

The database relations of this API application is visualised using the [Entity Relationship Diagram](#r6). The three entities depicted within the diagram represent the tables in the database.

Each table has a primary key that is uniquely assigned to each record in the table. A table can have an attribute known as a foreign key that references another table's primary key. This is what will establish associations between each entity.

Using the ERD as an example, the runs table has an attribute named user_id (foreign key) which corresponds to an id (primary key) in the users table. This means that for each record in the runs table, it is directly related to one unique user.

In the ERD, the relations between each entity is represented through the crow's foot notation connecting the primary keys and the foreign keys.

- A user can add zero or many to the log, however a run that has been added to the log can only have one user. Therefore users have a zero or many relationship with runs, while a run has one and only one relationship with a user.
  
- A user can add zero or many reviews to a run, however a review that has been added to a run can only have one user. Therefore users have a zero or many relationship with reviews, while a review has a one and only one relationship with a user.

- A run can have zero or many reviews added to it, however a reviuew that has been added to a run is only associated with one run. Therefore runs have a zero or many relationship with reviews, while a review has a one and only one relationship with a run.

---

## (R10)

---

The task allocation and tracking of this project was completed solely on Trello. The use of such a plan was utilised in order to segment the entire projects into smaller much simpler tasks with individual due dates and prioritiy settings. A list of models and controllers was first created in order to better visualise the end product. From there each instance was broken down into smaller sub tasks in order to enhance efficiency and prevent brain fog. Each sub task was also issued with a priority rating to reflect urgency. Documentation requirements were also added to the trello board to be completed after the source code had been finalised. The trello board can be found below

![trello_board](docs/trello.PNG)

---

## References

1. [Trello](https://trello.com)
2. [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)
3. [Flask-Marshmallow](https://pypi.org/project/flask-marshmallow/)
4. [Flask-Bcrypt](https://pypi.org/project/Flask-Bcrypt/)
5. [Flask-JWTExtended](https://pypi.org/project/Flask-JWT-Extended/)
6. [psycopg2](https://pypi.org/project/psycopg2/)
7. [python-dotenv](https://pypi.org/project/python-dotenv/)
8. [lucid.app](https://lucid.app/)
