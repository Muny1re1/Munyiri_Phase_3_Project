import sqlite3

CONN = sqlite3.connect('stocks.db')
CURSOR = CONN.cursor()
