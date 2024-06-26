# Env Viewer App

This is a simple Flask application that prints all your environment variables in a web page.

## Project Structure

```
env_viewer/
├── env_viewer/
│   ├── __init__.py
│   ├── app.py
│   ├── templates/
│   │   └── index.html
├── tests/
│   ├── __init__.py
│   ├── test_app.py
├── .editorconfig
├── .gitignore
├── Taskfile.yml
├── pyproject.toml
├── README.md
└── venv/
```

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/env_viewer.git
cd env_viewer
```

### 2. Set Up the Virtual Environment

```sh
python -m venv venv
source venv/bin/activate
```

### 3. Install Poetry

```sh
pip install poetry
```

### 4. Install Dependencies

```sh
poetry install
```

### 5. Install Task

Follow the installation instructions for installing [Task](https://taskfile.dev/).

## Running the Application

You can use Taskfile to run the application:

```sh
task run
```

This will start the Flask development server. Open your web browser and navigate to `http://127.0.0.1:5000` to see your local environment variables.

## Running the tests

You can use the Taskfile to run the tests:

```sh
task test
```

This will run the tests using pytest.
