from tradingview_ta import TA_Handler, Interval, Exchange
from Models.Indicator import Indicator
from Indicators.Setup import Setup as IndicatorsSetup
import sys, time

class TradingView_TA:
    intervals = [
        #Interval.INTERVAL_1_MINUTE,
        Interval.INTERVAL_5_MINUTES,
        #Interval.INTERVAL_15_MINUTES,
        Interval.INTERVAL_1_HOUR,
        Interval.INTERVAL_4_HOURS,
        Interval.INTERVAL_1_DAY,
        #Interval.INTERVAL_1_WEEK,
    ]
    
    score = {
        'STRONG_BUY': 5,
        'BUY': 2,
        'NEUTRAL': 0,
        'SELL': 2,
        'STRONG_SELL': -5
    }


    def __init__(self, should_print = False):
        self.should_print = should_print

    
    def fetch_ta(self, symbol):
        indicators = []

        for timeframe in self.intervals:
            try:
                pair_ta = TA_Handler(
                    symbol=symbol,
                    screener="crypto",
                    exchange="BINANCE",
                    interval=timeframe
                )
                
                for indicator_key, indicator_class in IndicatorsSetup.config.items():
                    print('indicator key:' + indicator_key)
                    print('indicator class:' + str(indicator_class))
                    
                    indicator = indicator_class(pair_ta)
                    indicator_value = indicator.calculate()
                    print('indicator value:' + str(indicator_value))

                    indicators.append(
                        Indicator(
                            key = indicator_key,
                            value =  indicator_value,
                            timeframe =  timeframe,
                            symbol =  symbol
                        )
                    )
                
                time.sleep(2)
            except:
                print( "Error fetching {}-{}".format(symbol,timeframe) )

        return indicators
