# FastAPI Starter Kit
## Features:
* FastAPI project structure tree
* user module
    - id, first name, last name, **email** as username, **password**, role, is_active created_at, updated_at 
* admin dashboard => sqladmin
* authentication => JWT
* db migration => alembic
* CORS middleware

## Structured Tree
```sh
├── alembic     # Manages database migrations
├── alembic.ini
├── app
│   ├── api
│   │   ├── endpoints   # Contains modules for each feature (user, product, payments).
│   │   │   ├── __init__.py
│   │   │   └── user
│   │   │       ├── auth.py
│   │   │       ├── functions.py
│   │   │       ├── __init__.py
│   │   │       └── user.py
│   │   ├── __init__.py
│   │   └── routers     # Contains FastAPI routers, where each router corresponds to a feature.
│   │       ├── api.py
│   │       ├── __init__.py
│   │       └── user.py
│   ├── core    # Contains core functionality like database management, dependencies, etc. 
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── __init__.py
│   ├── main.py     # Initializes the FastAPI app and brings together various components.
│   ├── models      # Contains modules defining database models for users, products, payments, etc.
│   │   ├── admin.py
│   │   ├── common.py
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── user.py
│   └── utils       # Can include utility functions that are used across different features.
├── requirements.txt # Lists project dependencies.
```
**app/api/endpoints/**: Contains modules for each feature (user, product, payments).

**app/api/routers/**: Contains FastAPI routers, where each router corresponds to a feature.

**app/models/**: Contains modules defining database models for users, products, payments, etc.

**app/core/**: Contains core functionality like database management, dependencies, etc.

**app/utils/**: Can include utility functions that are used across different features.

**app/main.py**: Initializes the FastAPI app and brings together various components.

**tests/**: Houses your test cases.

**alembic/**: Manages database migrations.

**docs/**: Holds documentation files.

**scripts/**: Contains utility scripts.

**requirements.txt**: Lists project dependencies.


# Setup
The first thing to do is to clone the repository:
```sh
$ https://github.com/MahmudJewel/fastapi-starter-kit
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ cd fastapi-starter-kit
$ python -m venv venv
$ source venv/bin/activate
```
Then install the dependencies:
```sh
# for fixed version
(venv)$ pip install -r requirements.txt

# or for updated version
(venv)$ pip install -r dev.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
# db migrations
(venv)$ alembic upgrade head

# start the server 
(venv)$ uvicorn app.main:app --reload
```

## User module's API
| SRL | METHOD | ROUTE | FUNCTIONALITY | Required Fields | 
| ------- | ------- | ----- | ------------- | ------------- |
| *1* | *POST* | ```/login``` | _Login user_| _email, password_|
| *2* | *POST* | ```/users/``` | _Create new user_|_email, password_|
| *3* | *GET* | ```/users/``` | _Get all users list_|_None_|
| *4* | *GET* | ```/users/me/``` | _Get current user details_|_None_|
| *5* | *GET* | ```/users/{user_id}``` | _Get indivisual users details_|_None_|
| *6* | *PATCH* | ```/users/{user_id}``` | _Update the user partially_|_email, password, is_active, role_|
| *7* | *DELETE* | ```/users/{user_id}``` | _Delete the user_|_None_| _admin_|
| *8* | *GET* | ```/``` | _Home page_|_None_|
| *9* | *GET* | ```/admin``` | _Admin Dashboard_|_None_|


# Tools
### Back-end
#### Language:
	Python

#### Frameworks:
	FastAPI
    pydantic
	
#### Other libraries / tools:
	SQLAlchemy
    starlette
    uvicorn
    python-jose
    alembic

# Happy Coding
## From ==> Mahmud

