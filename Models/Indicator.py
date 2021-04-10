class Indicator:
    
    def __init__(self, key, value, timeframe, symbol):
        self.key = key
        self.value = value
        self.timeframe = timeframe
        self.symbol = symbol
        self.pair_id = 0
        self.batch_id = 0


    def has_pair_id(self):
        return self.pair_id > 0


    def has_batch_id(self):
        return self.batch_id > 0
 