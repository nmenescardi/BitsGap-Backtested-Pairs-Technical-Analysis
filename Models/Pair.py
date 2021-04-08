
class Pair:
    
    categories = [] #TODO enum

    def __init__(self, symbol_str, profit_str = "", category = 'MONTH', exchanger = 'BINANCE'):
        self.symbol = self.massage_text_symbol( symbol_str )
        self.profit = self.massage_profit_number( profit_str )
        self.category = category
        self.exchanger = exchanger


    def massage_text_symbol(self, symbol_str):
        return symbol_str #TODO: remove / and spaces

        
    def massage_profit_number(self, profit_str):
        return profit_str #TODO: remove % (percentage sign) and return a float
