# API Testing Framework

A Python-based REST API testing framework built with **Pytest** and **Requests**, using the ReqRes API as the test environment.

The project demonstrates API test automation, reusable API client architecture, authentication testing, configuration management, and automated test execution.

## Tech Stack

- Python 3.12
- Pytest 9.1.1
- Requests 2.34.2
- python-dotenv 1.2.2
- ReqRes REST API

## Project Structure

```text
api-testing-framework/
│
├── api/
│   ├── __init__.py
│   ├── base_api.py
│   └── users_api.py
│
├── data/
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_authentication.py
│   ├── test_create_user.py
│   ├── test_delete_user.py
│   ├── test_get_users.py
│   ├── test_patch_user.py
│   └── test_update_user.py
│
├── utils/
│   ├── __init__.py
│   └── config.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Features

- Reusable API client built with Python classes and inheritance.
- Centralized HTTP request handling.
- Support for GET, POST, PUT, PATCH, and DELETE methods.
- Persistent HTTP session using `requests.Session()`.
- Request timeout configuration.
- API key authentication.
- Environment-based configuration using `.env`.
- Automated resource cleanup through Pytest fixtures.
- Parameterized test cases.

## Test Coverage

| Category | Scenarios |
|---|---|
| Authentication | Invalid API keys |
| GET | User list, single user, non-existing users, invalid user ID |
| POST | User creation, empty payload, invalid JSON |
| PUT | Full resource update |
| PATCH | Partial resource update |
| DELETE | Resource deletion |

**Current test result: 14 passed.**

## Setup and Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd api-testing-framework
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
API_KEY=your_reqres_api_key
BASE_URL=https://reqres.in
```

Replace the placeholder with your own valid ReqRes API key.

**Never commit your `.env` file or expose your API key publicly.**

## Running Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Run a specific test file:

```bash
python -m pytest tests/test_get_users.py -v
```

Run tests by category:

```bash
python -m pytest tests/test_create_user.py -v
```

## Framework Architecture

- `BaseAPI`: Handles common HTTP methods, shared headers, session management, and request timeouts.
- `UsersAPI`: Provides user-specific API operations through inheritance.
- `conftest.py`: Creates and manages the API client fixture.
- `config.py`: Loads and validates environment variables.
- `tests/`: Contains automated API test cases.

## Notes

This project uses ReqRes as a simulated REST API environment. Write, update, and delete operations demonstrate API request and response handling; they should not be interpreted as proof of persistent database changes.

## Author

QA Automation Portfolio Project