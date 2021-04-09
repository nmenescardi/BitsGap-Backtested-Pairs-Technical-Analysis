from dotenv import load_dotenv
import time, sys, json, os
from Models.Bitsgap import Bitsgap
from Models.Credentials import Credentials
from Data.Pairs import Pairs as PairsDAO
from Data.Batches import Batches as BatchesDAO

class PairsFetcher:
    
    def __init__(self):
        self.pairs_dao = PairsDAO()
        self.batches_dao = BatchesDAO()
    
    def run(self):
        # Load Env variables:
        load_dotenv()
        max_number_of_pairs = int(os.getenv("MAX_NUMBER_OF_PAIRS"))
        bitsgap_email = os.getenv("BITSGAP_EMAIL")
        bitsgap_password = os.getenv("BITSGAP_PASSWORD")

        credentials = Credentials(bitsgap_email, bitsgap_password)

        bitsgap = Bitsgap(credentials, max_number_of_pairs, should_print = True)

        bitsgap.login()
        
        pairs = set()
        pairs.update( 
            bitsgap.get_month(),
            bitsgap.get_week(),
            bitsgap.get_three_days()
        )

        bitsgap.cleanup()

        batch_id = self.batches_dao.new()
        #print('Batch ID:' + str(batch_id))

        for pair in pairs:            
            self.pairs_dao.insert(pair)
            pair.batch_id = batch_id
            pair.pair_id = self.pairs_dao.get_pair_id_by_symbol(pair.symbol)
            
        
        # Foreach pair:
            #TODO: insert 'batches_pairs' with previous IDs and profit + category
        #
