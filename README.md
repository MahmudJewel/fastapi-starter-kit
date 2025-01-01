# FastAPI Starter Kit
A professional FastAPI template
<p>
    <a href="https://github.com/MahmudJewel/fastapi-starter-boilerplate/fork">
        <img src="https://img.shields.io/github/forks/MahmudJewel/fastapi-starter-kit.svg?style=social&label=Fork" />
    </a>
    <a href="https://github.com/MahmudJewel/fastapi-starter-boilerplate/fork">
        <img src="https://img.shields.io/github/stars/MahmudJewel/fastapi-starter-kit.svg?style=social&label=Stars" />
    </a>
    <a href="https://github.com/MahmudJewel/fastapi-starter-boilerplate/fork">
        <img src="https://img.shields.io/nuget/dt/Azylee.Core.svg" />
    </a>
</p>
<p>
    If the repo is helpful, please give a star and fork it.
</p>
<a href="https://github.com/MahmudJewel/fastapi-starter-boilerplate/fork">
    Click here to clone/fork the repository
</a>

<!-- [![Fork](https://img.shields.io/github/forks/MahmudJewel/fastapi-starter-kit.svg?style=social&label=Fork)](https://github.com/MahmudJewel/fastapi-starter-kit/fork)
[![Stars](https://img.shields.io/github/stars/MahmudJewel/fastapi-starter-kit.svg?style=social&label=Stars)](https://github.com/MahmudJewel/fastapi-starter-kit)
[![NuGet](https://img.shields.io/nuget/dt/Azylee.Core.svg)](https://www.nuget.org/packages/Azylee.Core)   -->

## Features:

- FastAPI project structure tree
- user module
  - id, first name, last name, **email** as username, **password**, role, is_active created_at, updated_at
- admin dashboard => sqladmin
- authentication => JWT
- db migration => alembic
- CORS middleware

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
│   │       ├── main_router.py
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
│   ├── schemas   # Pydantic model for data validation
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
$ https://github.com/MahmudJewel/fastapi-starter-boilerplate
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ cd fastapi-starter-boilerplate
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
(venv)$ fastapi dev app/main.py # using fastapi CLI ==> after version 0.100.0
or
(venv)$ uvicorn app.main:app --reload # using directly uvicorn ==> old one => before version 0.100.0
```

## User module's API

| SRL | METHOD   | ROUTE              | FUNCTIONALITY                  | Fields                                                                                |
| --- | -------- | ------------------ | ------------------------------ | ------------------------------------------------------------------------------------- |
| _1_ | _POST_   | `/login`           | _Login user_                   | _**email**, **password**_                                                             |
| _2_ | _POST_   | `/refresh/?refresh_token=`           | _Refresh access token_|_None_ 
| _3_ | _POST_   | `/users/`          | _Create new user_              | _**email**, **password**, first name, last name_                                      |
| _4_ | _GET_    | `/users/`          | _Get all users list_           | _email, password, first name, last name, role, is_active, created_at, updated_at, id_ |
| _5_ | _GET_    | `/users/me/`       | _Get current user details_     | _email, password, first name, last name, role, is_active, created_at, updated_at, id_ |
| _6_ | _GET_    | `/users/{user_id}` | _Get indivisual users details_ | _email, password, first name, last name, role, is_active, created_at, updated_at, id_ |
| _7_ | _PATCH_  | `/users/{user_id}` | _Update the user partially_    | _email, password, is_active, role_                                                    |
| _8_ | _DELETE_ | `/users/{user_id}` | _Delete the user_              | _None_                                                                                |
| _9_ | _GET_    | `/`                | _Home page_                    | _None_                                                                                |
| _10_ | _GET_    | `/admin`           | _Admin Dashboard_              | _None_                                                                                |

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

For production level project, Please follow this repo https://github.com/MahmudJewel/fastapi-production-boilerplate
### Happy Coding
