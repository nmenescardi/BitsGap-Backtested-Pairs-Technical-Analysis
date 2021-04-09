class Indicator:
    
    def __init__(self, key, value, timeframe):
        self.key = key
        self.value = value
        self.timeframe = timeframe
        self.batch_id = 0
        self.pair_id = 0
