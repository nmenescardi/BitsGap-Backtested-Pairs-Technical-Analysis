
from Data.Indicators import Indicators as IndicatorsDAO
from Models.TradingView_TA import TradingView_TA
from Jobs.AbstractJob import AbstractJob

class TaDispacher(AbstractJob):
    
    def __init__(self, pairs):
        self.pairs = pairs
        self.indicators_dao = IndicatorsDAO()


    def run(self):
        tv_ta = TradingView_TA( should_print=True )

        for pair in self.pairs:
            indicators = tv_ta.fetch_ta(pair)
            
            for indicator in indicators:
                self.indicators_dao.insert(indicator)
