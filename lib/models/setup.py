from .connection import (CONN, CURSOR)

def create_table():

    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS traders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trader_name TEXT NOT NULL
        )
    ''')
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stock_name TEXT NOT NULL,
            rate_per_stock REAL NOT NULL
        )
    ''')
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trade_type TEXT NOT NULL,
            amount REAL NOT NULL,
            trader_id INTEGER,
            stock_id INTEGER,
            FOREIGN KEY (trader_id) REFERENCES traders (id),
            FOREIGN KEY (stock_id) REFERENCES stocks (id)
        )
    ''')

    CONN.commit()