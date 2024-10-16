
# Rule Engine with AST

This project implements a simple 3-tier rule engine application using Abstract Syntax Trees (AST) to represent conditional rules. It allows for dynamic creation, combination, and modification of rules to determine user eligibility based on attributes like age, department, income, and experience.

## Features

- Create and store rules using a simple string syntax
- Combine multiple rules into a single AST
- Evaluate user data against stored rules
- Simple web interface for rule creation and evaluation

## Technologies Used

- Backend: Python 3.7+, Flask
- Frontend: HTML, JavaScript
- Database: SQLite

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Vaibhavbasidoni/Initial-commit-of-Rule-Engine-with-AST.git
   cd rule-engine-ast
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Create a rule using the web interface. Example rule:
   ```
   (age > 30 AND department = 'Sales') AND (salary > 50000 OR experience > 5)
   ```

2. Use the evaluation form to test the rule against sample data.

3. Create multiple rules and test combinations.

## Design Choices

- Abstract Syntax Tree (AST): Used to represent the hierarchical structure of rules, allowing for efficient parsing and evaluation.
- Flask: Chosen for its simplicity and ease of use in creating web applications with Python.
- SQLite: Used as a lightweight, serverless database solution for storing rules.

## Non-Functional Enhancements

- Input Validation: Implemented to ensure rule strings are properly formatted before processing.
- Error Handling: Comprehensive error handling and reporting for both frontend and backend operations.


