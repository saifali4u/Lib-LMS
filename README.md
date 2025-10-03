# Library Management System

A Python-based CLI application for managing a library's books and members with JSON persistence.

## Setup
```bash
git clone <repo-url>
cd lms
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt

## Usage 
python cli.py add-book "Python 101" "Guido" 2020
python cli.py add-member "Alice" --admin
python cli.py list-books

## Run Tests
pytest -v