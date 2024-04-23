# FastAPI Library Management API

This is a FastAPI application for managing library resources. It provides endpoints to perform CRUD operations on books and manage library users.

## Requirements

- Python 3.7+
- FastAPI
- Pydantic
- Motor (for MongoDB)
- Uvicorn (or any ASGI server)
- Redis

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

- Ensure that you have MongoDB running locally or configure the connection details in `config/database.py`.
- Configure Redis connection details in `config/redis.py`.

## Usage

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## Endpoints

### Book Management

#### Create Book

- **Method:** POST
- **URL:** /books
- **Request Body:** JSON object representing book details
- **Response:** JSON object containing the ID of the newly created book

#### Fetch All Books

- **Method:** GET
- **URL:** /books
- **Query Parameters:** 
  - author (optional): Filter by author
  - genre (optional): Filter by genre
- **Response:** JSON array containing book data

#### Fetch Single Book

- **Method:** GET
- **URL:** /books/{id}
- **Response:** JSON object containing book details

#### Update Book

- **Method:** PATCH
- **URL:** /books/{id}
- **Request Body:** JSON object representing fields to update
- **Response:** 204 No Content if successful

#### Delete Book

- **Method:** DELETE
- **URL:** /books/{id}
- **Response:** 200 OK if successful

### User Management

#### Create User

- **Method:** POST
- **URL:** /users
- **Request Body:** JSON object representing user details
- **Response:** JSON object containing the ID of the newly created user

#### Fetch All Users

- **Method:** GET
- **URL:** /users
- **Response:** JSON array containing user data

#### Fetch Single User

- **Method:** GET
- **URL:** /users/{id}
- **Response:** JSON object containing user details

#### Update User

- **Method:** PATCH
- **URL:** /users/{id}
- **Request Body:** JSON object representing fields to update
- **Response:** 204 No Content if successful

#### Delete User

- **Method:** DELETE
- **URL:** /users/{id}
- **Response:** 200 OK if successful

## Rate Limiting

The API has a rate limiter middleware to restrict the number of requests per day per user. 

- **Limit:** 50 requests per day
- **Headers Required:** User ID (`user_id`)
- **Response:** 429 Too Many Requests if limit exceeded
- **Header:** `X-RateLimit-Remaining` shows the remaining requests

## Additional Features

- **Cross-Origin Resource Sharing (CORS) Middleware:** Enabled to allow all origins, methods, and headers.

## Root Endpoint

- **Method:** GET
- **URL:** /
- **Response:** "Welcome To The FastAPI Project!!"
