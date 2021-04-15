
class TradingViewList:

    def __init__(self, pairs, writer):
        self.pairs = self._format_pairs(pairs)
        self.writer = writer

        
    def _format_pairs(self, pairs):
        try:
            return list(pairs.keys())
        except:
            return pairs


    def create(self):
        content = (','.join(
            ['BINANCE:' + pair for pair in self.pairs]
        ))
        
        self.writer.log(content)
