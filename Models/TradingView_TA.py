from tradingview_ta import TA_Handler, Interval, Exchange
from Models.Indicator import Indicator
from Indicators.Setup import Setup as IndicatorsSetup
import sys, time

class TradingView_TA:
    intervals = [
        Interval.INTERVAL_1_MINUTE,
        Interval.INTERVAL_5_MINUTES,
        Interval.INTERVAL_15_MINUTES,
        Interval.INTERVAL_1_HOUR,
        Interval.INTERVAL_4_HOURS,
        Interval.INTERVAL_1_DAY,
        Interval.INTERVAL_1_WEEK,
    ]


    def __init__(self):
        self.indicators_setup = IndicatorsSetup()

    
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
                
                for indicator_class in self.indicators_setup.get_config():
                    indicator = indicator_class(pair_ta)
                    indicator_key = indicator.key()
                    indicator_value = indicator.calculate()

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
