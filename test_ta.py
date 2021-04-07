from tradingview_ta import TA_Handler, Interval, Exchange
import time, sys

def print_results(pair_ta, pair, interval_i):
    header_str = "{}-{}".format(pair, interval_i)
    print(header_str)
    
    body_str = "Summary: {}. Oscillators: {}. MAs: {}".format(
        pair_ta.get_analysis().summary['RECOMMENDATION'],
        pair_ta.get_analysis().oscillators['RECOMMENDATION'],
        pair_ta.get_analysis().moving_averages['RECOMMENDATION']
    )
    print(body_str)
    print("------------------------")
    #print(pair_ta.get_analysis().indicators)


pairs = [
    "BTCUSDT",
    "THETABTC",
]
intervals = [
    Interval.INTERVAL_1_MINUTE,
    Interval.INTERVAL_5_MINUTES,
    Interval.INTERVAL_1_HOUR,
    Interval.INTERVAL_4_HOURS,
    Interval.INTERVAL_1_DAY,
    Interval.INTERVAL_1_WEEK,
]

for pair in pairs:
    for interval_i in intervals:
        
        pair_ta = TA_Handler(
            symbol=pair,
            screener="crypto",
            exchange="BINANCE",
            interval=interval_i
        )
        print_results(pair_ta, pair, interval_i)
        sys.stdout.flush()
        time.sleep(2)
