from .connection import CONN, CURSOR
from .setup import create_table

class Stock:
    def __init__(self, stock_name, rate_per_stock, id=None):
        create_table()
        self._stock_name = None
        self._rate_per_stock = None
        self.stock_name = stock_name  
        self.rate_per_stock = rate_per_stock 
        self.id = id if id is not None else self.save_to_db()
    
    @property
    def stock_name(self):
        return self._stock_name

    @stock_name.setter
    def stock_name(self, stock_name):
        if self._stock_name is not None:
            raise AttributeError("Stock name has already been set!")
        if not (isinstance(stock_name, str) and len(stock_name) > 0):
            raise ValueError("Stock name must be a non-empty string!")
        self._stock_name = stock_name
    
    @property
    def rate_per_stock(self):
        return self._rate_per_stock
    
    @rate_per_stock.setter
    def rate_per_stock(self, rate_per_stock):
        if self._rate_per_stock is not None:
            raise AttributeError("Rate per stock has already been set!")
        if not isinstance(rate_per_stock, (float, int)):  # Allow both float and int
            raise ValueError("Rate per stock must be a number!")
        self._rate_per_stock = float(rate_per_stock)

    def save_to_db(self):
        sql = """
            INSERT INTO stocks 
            (stock_name, rate_per_stock) 
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.stock_name, self.rate_per_stock))
        CONN.commit()
        self.id = CURSOR.lastrowid
        return self.id

    def delete_from_db(self):
        sql = """
            DELETE FROM stocks WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM stocks
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]

    @classmethod
    def find_by_id(cls, stock_id):
        sql = """
            SELECT * FROM stocks WHERE id = ?
        """
        CURSOR.execute(sql, (stock_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(row[1], row[2], row[0])
        return None