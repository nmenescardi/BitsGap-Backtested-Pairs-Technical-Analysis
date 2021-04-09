from Jobs.PairsFetcher import PairsFetcher
from Jobs.BatchSaver import BatchSaver


fetcher = PairsFetcher()
pairs = fetcher.run()

batch_saver = BatchSaver(pairs)
batch_saver.run()
