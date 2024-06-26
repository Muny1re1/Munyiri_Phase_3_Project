# Stock Trade Tracker CLI

## Introduction
The Stock Trade Tracker CLI is a command-line interface application designed to manage traders, stocks, and trades. It provides functionalities to create traders and stocks, record trades between traders and stocks, and view, delete, or update trader information. This project utilizes an Object-Relational Mapping (ORM) approach to interact with a SQLite database, ensuring efficient data storage and retrieval.

## Directory Structure
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py
    ├── models
    │   ├── connection.py
    │   ├── setup.py
    │   ├── __init__.py
    │   ├── trader.py
    │   ├── stock.py
    │   └── trade.py
    ├── debug.py
    └── helpers.py

## Getting Started
### Installation:

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies using pipenv install.
4. Activate the virtual environment using pipenv shell.
5. Running the CLI:
6. Execute python lib/cli.py to start the CLI application.
7. Follow the on-screen prompts to interact with the application.

## Features
### Trader Management
Create Trader: Add new traders with their names.
View All Traders: Display a list of all traders.
Find Trader by ID: Retrieve trader details using their unique ID.
Delete Trader: Remove a trader from the system.

### Stock Management
Create Stock: Register new stocks with their names.
View All Stocks: List all available stocks.
Find Stock by ID: Fetch stock information using its ID.
Delete Stock: Delete a stock from the database.

### Trade Management
Record Trade: Log transactions between traders and specific stocks.
View All Trades: Display a history of all recorded trades.
Find Trade by ID: Retrieve trade details using its unique ID.
Delete Trade: Remove a trade record from the database.

### Database Schema
The application uses SQLite as its database. Here's a simplified schema:

#### traders table:

1. id (INTEGER, PRIMARY KEY)
2. name (TEXT)

#### stocks table:

1. id (INTEGER, PRIMARY KEY)
2. name (TEXT)

#### trades table:

1. id (INTEGER, PRIMARY KEY)
2. trade_type (TEXT)
3. amount (REAL)
4. trader_id (INTEGER, FOREIGN KEY references traders(id))
5. stock_id (INTEGER, FOREIGN KEY references stocks(id))

### Testing
Unit tests for models are located in the tests directory.
Run tests using pytest to ensure all functionalities are working correctly.

### Dependencies
1. sqlite3: SQLite database management.
2. pytest: Testing framework for unit tests.
3. pipenv: Dependency management tool.

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.