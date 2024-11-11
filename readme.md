# URL Shortener with Click Analytics

A simple URL shortener built with **FastAPI** and **SQLModel** that allows users to shorten URLs and track the number of clicks on each shortened URL. This application demonstrates how to implement URL shortening and analytics using FastAPI and SQLModel.

## Features

- **URL Shortening**: Shorten long URLs into compact, shareable links.
- **Click Analytics**: Track and view the number of clicks on each shortened URL.
- **FastAPI**: A fast and modern web framework for building APIs with Python.
- **SQLModel**: A modern ORM for SQL-based databases, providing easy integration with SQLAlchemy and Pydantic.

## Requirements

- Python 3.8+
- FastAPI
- SQLModel
- Uvicorn (for development server)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/emmanuel1-byte/click-shortener.git
cd url-shortener

````

```markdown
### 2. Set up a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

Make sure your database (/PostgreSQL/MySQL) is set up and configured.

### 5. Start the application

You can start the FastAPI development server using Uvicorn:

```bash
uvicorn main:app --reload
```

The application should now be running at `http://127.0.0.1:8000`.

## API Documentation

The API documentation is automatically generated using **Swagger UI** and can be accessed at the following URL:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
```
