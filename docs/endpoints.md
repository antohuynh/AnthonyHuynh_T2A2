# API Endpoints Documentation (R5)

---

## Table of Contents

[Auth Routes](#auth-routes)

[User Routes](#user-routes)

[Admin Routes](#admin-routes)

[Run Routes](#run-routes)

[Error Handling Routes](#error-handling-routes)

[Return to README](../README.md)

---

## Auth Routes

---

### /auth/register/

- Methods: POST

- Arguments: None

- Description: Register new user in the database

- Authentication: None

- Authorization: None

- Request Body:

```json
{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "password": "123"
}
```

- Response Body:

```json
{
    "message": "You are now registered!",
    "user": {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "date_joined": "2022-11-18",
        "is_admin": false,
        "runs": [],
        "reviews": []
    }
}
```

### /auth/login/

- Methods: POST

- Arguments: none

- Description: User login

- Authentication: none

- Authorization: none

- Request Body:

```json
{
    "email": "johndoe@example.com",
    "password": "123"
}
```

- Response Body:

```json
{
    "message": "You have successfully logged in!",
    "email": "johndoe@example.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODMyNDg4MywianRpIjoiNTU1NzZhYmYtOWE0OS00ZjA5LWE4NDItMGU2ZDhmMTA2NzQwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjQiLCJuYmYiOjE2NjgzMjQ4ODMsImV4cCI6MTY2ODQxMTI4M30._zK4sbrjHG9twm18v7Oi1qLSyZMVcDS6-QOgBQVhQEY",
    "is_admin": false
}
```

---

## User Routes

---

/users/profile/

- Methods: GET

- Arguments: none

- Description: Read user profile

- Authentication: jwt_required

- Authorization: User owner only (get_jwt_identity)

- Request Body: none

- Response Body:

```json
{
  "id": 1,
  "name": "Marty Ngo",
  "email": "martyngo@example.com",
  "date_joined": "2022-04-27",
  "is_admin": false,
  "runs": [
    {
      "location": "Hurstville",
      "runtype": "Easy"
    },
    {
      "location": "Kogarah",
      "runtype": "Tempo"
    }
  ],
  "reviews": [
    {
      "id": 2,
      "description": "Was very difficult",
      "date": "2022-04-27",
      "run": {
        "location": "Hurstville",
        "runtype": "Easy"
      }
    }
  ]
}
```

/users/profile/

- Methods: PUT or PATCH

- Arguments: none

- Description: Update user details

- Authentication: jwt_required

- Authorization: User owner only (get_jwt_identity)

- Request Body:

```json
{
    "name": "Marty Ngo",
    "email": "martyngo@example.com",
    "password": "123"
}
```

- Response Body:

```json
{
    "message": "You have updated your details!",
    "user": {
        "id": 3,
        "name": "Marty Ngo",
        "email": "martinngo@example.com",
        "date_joined": "2022-04-27",
        "is_admin": false,
        
        "runs": [
            {
                "location": "Hurstville",
                "runtype": "Easy"
            },
            {
                "location": "Kogarah",
                "runtype": "Tempo"
            }
        ],
        "Reviews": [
            {
                "id": 2,
                "description": "Was very difficult",
                "date": "2022-04-27",
                "run": {
                    "location": "Hurstville",
                    "runtype": "Easy"
                }
            }
        ]
    }
}
```

---

## Admin Routes

---

/admin/<int:user_id>/give_admin/

- Methods: POST

- Arguments: user_id

- Description: Give admin permissions to a user

- Authentication: jwt_required

- Authorization: Admin only

- Request Body: none

- Response Body:

```json
{
  "message": "You have successfully given this user admin permissions."
}
```

/admin/<int:user_id>/remove_admin/

- Methods: POST

- Arguments: user_id

- Description: Remove admin permissions from a user

- Authentication: jwt_required

- Authorization: Admin only

- Request Body: none

- Response Body:

```json
{
  "message": "You have successfully removed admin permissions from this user."
}
```

/admin/all_users/

- Methods: GET

- Arguments: none

- Description: Retrieve all registered users profiles

- Authentication: jwt_required

- Authorization: Admin only

- Request Body: none

- Response Body:

```json
[
    {
        "id": 1,
        "name": null,
        "email": "admin@runninglog.com",
        "date_joined": null,
        "is_admin": true,
        "runs": [],
        "reviews": []
    },
    {
        "id": 2,
        "name": "Tino Nugent",
        "email": "tinonugent@example.com",
        "date_joined": "2020-01-26",
        "is_admin": false,
        "runs": [
            {
                "location": "Strathfield",
                "runtype": "Long Run"
            }
        ],
        "reviews": [
            {
                "id": 1,
                "description": "Just set a PB!",
                "date": "2022-11-18",
                "run": {
                    "location": "Strathfield",
                    "runtype": "Long Run"
                }
            }
           
        ]
    },
    {
        "id": 6,
        "name": "Test Subject",
        "email": "test@example.com",
        "date_joined": "2022-11-13",
        "is_admin": false,
        "runs": [],
        "reviews": []
    },
    {
        "id": 3,
        "name": "Marty Ngo",
        "email": "martyngo@example.com",
        "date_joined": "2021-04-27",
        "is_admin": false,
        "runs": [
            {
                "location": "Hurstville",
                "runtype": "Easy"
            },
            {
                "location": "Kogarah",
                "runtype": "Tempo"
            }
        ],
        "reviews": [
            {
                "id": 2,
                "description": "Was very difficult",
                "date": "2022-04-27",
                "run": {
                    "location": "Hurstville",
                    "runtype": "Easy"
                }
            }
        ]
    }
]
```

/admin/user/<int:user_id>/

- Methods: GET

- Arguments: user_id

- Description: Retrieve one user's profile

- Authentication: jwt_required

- Authorization: Admin only

- Request Body: none

- Response Body:

```json
{
        "id": 2,
        "name": "Tino Nugent",
        "email": "tinonugent@example.com",
        "date_joined": "2020-01-26",
        "is_admin": false,
        "runs": [
            {
                "location": "Strathfield",
                "runtype": "Long Run"
            }
        ],
        "reviews": [
            {
                "id": 1,
                "description": "Just set a PB!",
                "date": "2022-11-18",
                "run": {
                    "location": "Strathfield",
                    "runtype": "Long Run"
                }
            }
           
        ]
    }
```

/admin/user/<int:user_id>/

- Methods: PUT or PATCH

- Arguments: user_id

- Description: Update a user's profile

- Authentication: jwt_required

- Authorization: Admin only

- Request Body:

```json
{
    "email": "tinonugnet@gmail.com",
}
```

- Response Body:

```json
{
        "id": 2,
        "name": "Tino Nugent",
        "email": "tinonugent@example.com",
        "date_joined": "2020-01-26",
        "is_admin": false,
        "runs": [
            {
                "location": "Strathfield",
                "runtype": "Long Run"
            }
        ],
        "reviews": [
            {
                "id": 1,
                "description": "Just set a PB!",
                "date": "2022-11-18",
                "run": {
                    "location": "Strathfield",
                    "runtype": "Long Run"
                }
            }
           
        ]
    }
```

/admin/user/<int:user_id>/

- Methods: DELETE

- Arguments: user_id

- Description: Delete user profile

- Authentication: jwt_required

- Authorization: Admin only

- Request Body: none

- Response Body:

```json
{
    "message": "You have successfully deleted this user.",
    "user_id": 6,
    "name": "Test Subject",
    "email": "test@example.com"
}
```

---

## Run Routes

---

/runs/

- Methods: GET

- Arguments: none

- Description: Retrieve all runs added to the log

- Authentication: none

- Authorization: none

- Request Body: none

- Response Body:

```json
[
    {
        "id": 1,
        "location": "Hurstville",
        "distance": "5",
        "runtype": "Easy",
        "rpe": "10",
        "date_tracked": "2022-11-13",
        "user": {
            "name": "Marty Ngo",
            "email": "martyngo@example.com"
        },
        "reviews": [
            {
                "id": 2,
                "location": "Was very difficult",
                "date": "2022-11-13",
                "user": {
                    "name": "Marty Ngo",
                    "email": "martyngo@example.com"
                }
            }
        ]
    },
    {
        "id": 2,
        "location": "Strathfield",
        "distance": "20",
        "runtype": "Long Run",
        "rpe": "8",
        "date_tracked": "2022-11-13",
        "user": {
            "name": "Tino Nugent",
            "email": "tinonugent@example.com"
        },
        "reviews": [
            {
                "id": 1,
                "description": "Just set a PB",
                "date": "2022-11-13",
                "user": {
                    "name": "Tino Nugent",
                    "email": "tinonugent@example.com"
                }
            }
        ]
    },
    {
        "id": 3,
        "location": "Kogarah",
        "distance": "5",
        "runtype": "Tempo",
        "rpe": "7",
        "date_tracked": "2022-04-27",
        "user": {
            "name": "Marty Ngo",
            "email": "martyngo@example.com"
        }
        
        
    }
]
```

/runs/<int:run_id>/

- Methods: GET

- Arguments: run_id

- Description: Retrieve one run from log

- Authentication: none

- Authorization: none

- Request Body: none

- Response Body:

```json
{
    "id": 2,
    "location": "Hurstville",
    "distance": "5",
    "runtype": "Easy",
    "rpe": "10",
    "date_tracked": "2022-04-27",
    "user": {
        "name": "Marty Ngo",
        "email": "martyngo@example.com"
    },
    "reviews": [
        {
            "id": 1,
            "description": "Was very difficult",
            "date": "2022-04-27",
            "user": {
                "name": "Marty Ngo",
                "email": "martyngo@example.com"
            }
        }
    ]
}
```

/runs/

- Methods: POST

- Arguments: none

- Description: Create/add run to log

- Authentication: jwt_required

- Authorization: none

- Request Body:

```json
{
  "location": "Berala",
  "distance": "7",
  "runtype": "Easy",
  "rpe": "5",
}
```

- Response Body:

```json
{
    "message": "You have recorded your run!!",
    "run": {
        "id": 4,
        "location": "Berala",
        "distance": "7",
        "runtype": "Easy",
        "rpe": "5",
        "date_tracked": "2022-08-25",
        "user": {
            "name": "Anthony Huynh",
            "email": "ah@gmail.com"
        },
        "reviews": []
    }
}
```

/runs/<int:run_id>/

- Methods: PUT or PATCH

- Arguments: run_id

- Description: Update run details

- Authentication: jwt_required

- Authorization: User owner i.e. user who added the run (get_jwt_identity) or Admin only

- Request Body:

```json
{
    "rpe": "7"
}
```

- Response Body:

```json
{
    "message": "You have recorded your run!!",
    "run": {
        "id": 4,
        "location": "Berala",
        "distance": "7",
        "runtype": "Easy",
        "rpe": "7",
        "date_tracked": "2022-08-25",
        "user": {
            "name": "Anthony Huynh",
            "email": "ah@gmail.com"
        },
        "reviews": []
    }
}
```

/runs/<int:run_id>/

- Methods: DELETE

- Arguments: run_id

- Description: Delete run from log

- Authentication: jwt_required

- Authorization: User owner i.e. user who added the run (get_jwt_identity) or Admin only

- Request Body: none

- Response Body:

```json
{
    "message": "Your run has been deleted!"
}
```

/runs/<int:run_id>/reviews/

- Methods: GET

- Arguments: run_id

- Description: Retrieve all reviews on a run

- Authentication: none

- Authorization: none

- Request Body: none

- Response Body:

```json
{
    "id": 2,
    "description": "Was very difficult",
    "date": "2022-04-27",
    "user": {
        "name": "Marty Ngo",
        "email": "martyngo@example.com"
    }
}
```

/runs/reviews/<int:review_id>/

- Methods: GET

- Arguments: review_id

- Description: Retrieve one review

- Authentication: none

- Authorization: none

- Request Body: none

- Response Body:

```json
{
    "id": 2,
    "description": "Was very difficult",
    "date": "2022-04-27",
    "user": {
        "name": "Marty Ngo",
        "email": "martyngo@example.com"
    }
}
```

/runs/<int:run_id>/reviews/

- Methods: POST

- Arguments: run_id

- Description: Add a review for a logged run

- Authentication: jwt_required

- Authorization: none

- Request Body:

```json
{
    "description": "I can now run this route without stopping",
}
```

- Response Body:

```json
{
    "message": "You have successfully created a review",
    "review": {
        "id": 4,
        "description": "I can now run this route without stopping",
        "date": "2022-11-18",
        "user": {
            "name": "Marty Ngo",
            "email": "martyngo@example.com"
        }
    }
}
```

/runs/reviews/<int:review_id>/

- Methods: PUT or PATCH

- Arguments: review_id

- Description: Update a review

- Authentication: jwt_required

- Authorization: User owner i.e. user who added the review (get_jwt_identity) or Admin only

- Request Body:

```json
{
    "description": "Was very easy"
}
```

- Response Body:

```json
{
    "message": "You have updated your review!",
    "review": {
        "id": 2,
        "description": "Was very easy",
        "date": "2022-04-27",
        "run": {
            "location": "Hurstville",
            "runtype": "Easy"
        },
        "user": {
            "name": "Marty Ngo",
            "email": "martyngo@example.com"
        }
    }
}
```

/runs/reviews/<int:review_id>/

- Methods: DELETE

- Arguments: review_id

- Description: Delete a review

- Authentication: jwt_required

- Authorization: User owner i.e. user who added the review (get_jwt_identity) or Admin only

- Request Body: none

- Response Body:

```json
{
    "message": "This review has been deleted."
}
```

---

## Error Handling Routes

---

### **Response Status Code 400: Bad Request**

ValidationError:

User attempts to register with an invalid email:

```json
{
    "error": "{'email': ['Not a valid email address.']}"
}
```

KeyError

User attempts to register without providing an email or password:

```json
{
    "error": "The field 'email/password' is required."
}
```

### **Response Status Code 401: Unauthorized**

User attempts to login with incorrect email or password (status code: 401):

```json
{
    "error": "Invalid email or password - please try again."
}
```

No admin authorization to perform request:

```json
{
    "error": "You do not have the appropriate permissions to perform this action."
}
```

### **Response Status Code 404: Not Found**

User attempts to retrieve a run that does not exist:

```json
{
    "error": "Run not found with id 5"
}
```

### **Response Status Code 409: Conflict**

User attempts to register with an email already in use:

```json
{
    "error": "Email address already in use"
}
```

[Table of Contents](#table-of-contents)

[Return to README](../README.md)

---
