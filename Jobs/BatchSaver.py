import time, sys, json, os
from Data.Pairs import Pairs as PairsDAO
from Data.Batches import Batches as BatchesDAO
from Data.BatchesPairs import BatchesPairs as BatchesPairsDAO
from Jobs.AbstractJob import AbstractJob

class BatchSaver(AbstractJob):
    
    def __init__(self, pairs):
        self.pairs = pairs
        self.pairs_dao = PairsDAO()
        self.batches_dao = BatchesDAO()
        self.batches_pairs_dao = BatchesPairsDAO()
    
    def run(self):
        self.batch_id = self.batches_dao.new()
        [self._insert(pair) for pair in self.pairs]

            
    def _insert(self, pair):
        self.pairs_dao.insert(pair)
        pair.batch_id = self.batch_id
        pair.pair_id = self.pairs_dao.get_pair_id_by_symbol(pair.symbol)
        self.batches_pairs_dao.insert(pair)
