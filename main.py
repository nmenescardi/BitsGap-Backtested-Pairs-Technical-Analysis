from Jobs.PairsFetcher import PairsFetcher
from Jobs.BatchSaver import BatchSaver

from Data.Pairs import Pairs as PairsDAO
from Data.Indicators import Indicators as IndicatorsDAO
from Models.TradingView_TA import TradingView_TA


fetcher = PairsFetcher()
pairs = fetcher.run()

batch_saver = BatchSaver(pairs)
batch_saver.run()


pairs_dao = PairsDAO()
indicators_dao = IndicatorsDAO()
btc_quote_pairs = pairs_dao.get_pairs_by_quote(quote = 'BTC', amount = 5)

tv_ta = TradingView_TA( should_print=True)

for pair in btc_quote_pairs:
    print(pair)
    indicators = tv_ta.fetch_ta(pair)
    
    for indicator in indicators:
        indicators_dao.insert(indicator)
