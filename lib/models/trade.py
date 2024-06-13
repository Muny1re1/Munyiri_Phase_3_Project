from .connection import CONN, CURSOR
from .setup import create_table
from .trader import Trader
from .stock import Stock

class Trade:
    def __init__(self, trade_type, amount, trader_id, stock_id, id=None):
        create_table()  # Ensure table exists
        self._trade_type = None
        self._amount = None
        self._trader_id = None
        self._stock_id = None
        self.trade_type = trade_type
        self.amount = amount
        self.trader_id = trader_id
        self.stock_id = stock_id
        self.id = id if id is not None else self.save_to_db()
    
    @property
    def trade_type(self):
        return self._trade_type
    
    @trade_type.setter
    def trade_type(self, trade_type):
        if self._trade_type is not None:
            raise AttributeError("Trade type has already been set!")
        if not isinstance(trade_type, str):
            raise ValueError("Trade type must be a string!")
        self._trade_type = trade_type
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        if self._amount is not None:
            raise AttributeError("Amount has already been set!")
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number!")
        self._amount = amount

    @property
    def trader_id(self):
        return self._trader_id
    
    @trader_id.setter
    def trader_id(self, trader_id):
        if self._trader_id is not None:
            raise AttributeError("Trader ID has already been set!")
        if not isinstance(trader_id, int):
            raise ValueError("Trader ID must be an integer!")
        self._trader_id = trader_id

    @property
    def stock_id(self):
        return self._stock_id
    
    @stock_id.setter
    def stock_id(self, stock_id):
        if self._stock_id is not None:
            raise AttributeError("Stock ID has already been set!")
        if not isinstance(stock_id, int):
            raise ValueError("Stock ID must be an integer!")
        self._stock_id = stock_id

    def save_to_db(self):
        sql = """
            INSERT INTO trades 
            (trade_type, amount, trader_id, stock_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.trade_type, self.amount, self.trader_id, self.stock_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        return self.id

    def delete_from_db(self):
        sql = """
            DELETE FROM trades WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM trades
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    @classmethod
    def find_by_id(cls, trade_id):
        sql = """
            SELECT * FROM trades WHERE id = ?
        """
        CURSOR.execute(sql, (trade_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(row[1], row[2], row[3], row[4], row[0])
        return None

    @classmethod
    def get_trades_by_trader_id(cls, trader_id):
        try:
            trader_id = int(trader_id)
        except ValueError:
            raise ValueError("Trader ID must be an integer!")

        sql = """
            SELECT * FROM trades WHERE trader_id = ?
        """
        CURSOR.execute(sql, (trader_id,))
        rows = CURSOR.fetchall()
        
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]