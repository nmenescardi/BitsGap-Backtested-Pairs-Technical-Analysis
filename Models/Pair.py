
class Pair:
    
    categories = [] #TODO enum

    def __init__(self, symbol_str, profit_str = "", category = 'MONTH', exchanger = 'BINANCE'):
        self.symbol = self.format_symbol( symbol_str )
        self.profit = self.format_profit( profit_str )
        self.category = category
        self.exchanger = exchanger


    def format_symbol(self, symbol_str):
        return symbol_str.replace(" ", "").replace("/", "")

        
    def format_profit(self, profit_str):
        return float(profit_str.replace(" ", "").replace("%", ""))
