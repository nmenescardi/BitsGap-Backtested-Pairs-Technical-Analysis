from tradingview_ta import TA_Handler, Interval, Exchange
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


    def __init__(self):
        pass

    
    def fetch_ta(self, pair):
        for interval_i in self.intervals:
            
            pair_ta = TA_Handler(
                symbol=pair,
                screener="crypto",
                exchange="BINANCE",
                interval=interval_i
            )
            self.print_result(pair_ta, pair, interval_i)
            time.sleep(2)

        
    def print_result(self, pair_ta, pair, interval):
        header_str = "{}-{}".format(pair, interval)
        print(header_str)
        body_str = "Summary: {}. Oscillators: {}. MAs: {}".format(
            pair_ta.get_analysis().summary['RECOMMENDATION'],
            pair_ta.get_analysis().oscillators['RECOMMENDATION'],
            pair_ta.get_analysis().moving_averages['RECOMMENDATION']
        )
        print(body_str)
        print("------------------------")
        sys.stdout.flush()
        #print(pair_ta.get_analysis().indicators)
