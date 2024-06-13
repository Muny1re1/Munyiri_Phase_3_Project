from helpers import exit_program
from models.trader import Trader
from models.stock import Stock
from models.trade import Trade

def display_menu():
    print("Welcome to the Stock Trade Tracker CLI")
    print("1. Create a Trader")
    print("2. Create a Stock")
    print("3. Create a Trade")
    print("4. View All Traders")
    print("5. View All Stocks")
    print("6. View All Trades")
    print("7. Find Trader by ID")
    print("8. Find Stock by ID")
    print("9. Find Trade by ID")
    print("10. Delete Trader")
    print("11. Delete Stock")
    print("12. Delete Trade")
    print("13. Find Trades by a trader")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            trader_name = input("Enter trader name: ")
            trader = Trader(trader_name)
            print(f"Trader {trader.trader_name} created with ID {trader.id}")
        elif choice == "2":
            stock_name = input("Enter stock name: ")
            rate_per_stock = float(input("Enter rate per stock: "))
            stock = Stock(stock_name, rate_per_stock)
            print(f"Stock {stock.stock_name} created with ID {stock.id}")
        elif choice == "3":
            trader_id = int(input("Enter trader ID: "))
            stock_id = int(input("Enter stock ID: "))
            trade_type = input("Enter trade type (profit/loss): ")
            amount = float(input("Enter amount: "))
            trader = Trader.find_by_id(trader_id)
            stock = Stock.find_by_id(stock_id)
            if trader and stock:
                trade = Trade(trade_type, amount, trader_id, stock_id)
                print(f"Trade created with ID {trade.id}")
            else:
                print("Invalid trader or stock ID")
        elif choice == "4":
            traders = Trader.get_all()
            for trader in traders:
                print(f"ID: {trader.id}, Name: {trader.trader_name}")
        elif choice == "5":
            stocks = Stock.get_all()
            for stock in stocks:
                print(f"ID: {stock.id}, Name: {stock.stock_name}, Rate: {stock.rate_per_stock}")
        elif choice == "6":
            trades = Trade.get_all()
            for trade in trades:
                trade_dict = {
                    "ID": trade.id,
                    "Type": trade.trade_type,
                    "Amount": trade.amount,
                    "Trader ID": trade.trader_id,
                    "Stock ID": trade.stock_id
                }
                print(trade_dict)
        elif choice == "7":
            trader_id = int(input("Enter trader ID: "))
            trader = Trader.find_by_id(trader_id)
            if trader:
                print(f"ID: {trader.id}, Name: {trader.trader_name}")
            else:
                print("Trader not found")
        elif choice == "8":
            stock_id = int(input("Enter stock ID: "))
            stock = Stock.find_by_id(stock_id)
            if stock:
                print(f"ID: {stock.id}, Name: {stock.stock_name}, Rate: {stock.rate_per_stock}")
            else:
                print("Stock not found")
        elif choice == "9":
            trade_id = int(input("Enter trade ID: "))
            trade = Trade.find_by_id(trade_id)
            if trade:
                trade_dict = {
                    "ID": trade.id,
                    "Type": trade.trade_type,
                    "Amount": trade.amount,
                    "Trader ID": trade.trader_id,
                    "Stock ID": trade.stock_id
                }
                print(trade_dict)
            else:
                print("Trade not found")
        elif choice == "10":
            trader_id = int(input("Enter trader ID: "))
            trader = Trader.find_by_id(trader_id)
            if trader:
                trader.delete_from_db()
                print(f"Trader {trader_id} deleted")
            else:
                print("Trader not found")
        elif choice == "11":
            stock_id = int(input("Enter stock ID: "))
            stock = Stock.find_by_id(stock_id)
            if stock:
                stock.delete_from_db()
                print(f"Stock {stock_id} deleted")
            else:
                print("Stock not found")
        elif choice == "12":
            trade_id = int(input("Enter trade ID: "))
            trade = Trade.find_by_id(trade_id)
            if trade:
                trade.delete_from_db()
                print(f"Trade {trade_id} deleted")
            else:
                print("Trade not found")
        elif choice == "13":
            trader_id = int(input("Enter trader ID: "))
            trades = Trade.get_trades_by_trader_id(trader_id)
            if trades:
                for trade in trades:
                    print(f"Trade ID: {trade.id}, Type: {trade.trade_type}, Amount: {trade.amount}, Trader ID: {trade.trader_id}, Stock ID: {trade.stock_id}")
            else:
                print("No trades found for this trader")
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()