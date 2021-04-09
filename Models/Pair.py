class Pair:
    
    categories = {
        '3_days'    : '3_DAYS',
        'Week'      : 'WEEK',
        'Month'     : 'MONTH'
    }

    def __init__(self, symbol_str, profit_str = '', category = categories['Month'], exchanger = 'BINANCE'):
        self.symbol = self.format_symbol( symbol_str )
        self.profit = self.format_profit( profit_str )
        self.category = category
        self.exchanger = exchanger
        self.batch_id = 0
        self.pair_id = 0


    def format_symbol(self, symbol_str):
        return symbol_str.replace(" ", "").replace("/", "")

        
    def format_profit(self, profit_str):
        return float(profit_str.replace(" ", "").replace("%", ""))


    def __hash__(self):
        return hash((self.symbol, self.profit, self.category, self.exchanger))


    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.symbol == other.symbol and self.exchanger == other.exchanger
