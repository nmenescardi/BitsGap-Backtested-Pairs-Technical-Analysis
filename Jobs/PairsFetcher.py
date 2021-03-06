import time, sys, json, os
from Models.Bitsgap import Bitsgap
from Models.Credentials import Credentials
from Jobs.AbstractJob import AbstractJob

class PairsFetcher(AbstractJob):

    def run(self):
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

        return pairs
