
from dotenv import load_dotenv
import time, sys, json, os
from Models.Bitsgap import Bitsgap
from Models.Credentials import Credentials

# Load Env variables:
load_dotenv()
max_number_of_pairs = int(os.getenv("MAX_NUMBER_OF_PAIRS"))
bitsgap_email = os.getenv("BITSGAP_EMAIL")
bitsgap_password = os.getenv("BITSGAP_PASSWORD")


credentials = Credentials(bitsgap_email, bitsgap_password)

bitsgap = Bitsgap(credentials, max_number_of_pairs)

bitsgap.login()
bitsgap.get_month()
#bitsgap.get_week()
#bitsgap.get_three_days()

bitsgap.cleanup()
