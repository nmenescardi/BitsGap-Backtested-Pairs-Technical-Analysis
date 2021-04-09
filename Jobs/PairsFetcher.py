from dotenv import load_dotenv
import time, sys, json, os
from Models.Bitsgap import Bitsgap
from Models.Credentials import Credentials
from Data.Pairs import Pairs as PairsDAO

class PairsFetcher:
    
    def __init__(self):
        self.pairs_dao = PairsDAO()
    
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

        #print('Pairs: ' + str(len(pairs)))
        #TODO: Insert a new 'batch' and get the 'batch_id'
        
        for pair in pairs:            
            self.pairs_dao.insert(pair)
        
        # Foreach pair:
            #TODO: save the 'pair enity' (symbol + exchanger) and get the 'pair_id'
            #TODO: insert 'batches_pairs' with previous IDs and profit + category
        #
