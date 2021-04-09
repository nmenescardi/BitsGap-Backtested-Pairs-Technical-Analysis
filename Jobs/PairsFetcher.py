from dotenv import load_dotenv
import time, sys, json, os
from Models.Bitsgap import Bitsgap
from Models.Credentials import Credentials
        
class PairsFetcher:
    
    def run(self):
        # Load Env variables:
        load_dotenv()
        max_number_of_pairs = int(os.getenv("MAX_NUMBER_OF_PAIRS"))
        bitsgap_email = os.getenv("BITSGAP_EMAIL")
        bitsgap_password = os.getenv("BITSGAP_PASSWORD")

        credentials = Credentials(bitsgap_email, bitsgap_password)

        bitsgap = Bitsgap(credentials, max_number_of_pairs, should_print = True)

        bitsgap.login()
        month_list = bitsgap.get_month()        
        week_list = bitsgap.get_week()
        three_days_list = bitsgap.get_three_days()

        bitsgap.cleanup()