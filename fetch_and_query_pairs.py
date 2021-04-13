from Jobs.PairsFetcher import PairsFetcher
from Jobs.BatchSaver import BatchSaver
from Jobs.TaDispacher import TaDispacher

from Data.Pairs import Pairs as PairsDAO


fetcher = PairsFetcher()
pairs = fetcher.run()

batch_saver = BatchSaver(pairs)
batch_saver.run()

pairs_dao = PairsDAO()
btc_quote_pairs = pairs_dao.get_pairs_by_quote(quote = 'BTC')
ta_dispacher = TaDispacher(btc_quote_pairs)
ta_dispacher.run()
