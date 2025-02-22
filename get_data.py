""""
Getting data and storing in Mongodb
"""


import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


class dataextraction():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv2json(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def data2mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    if __name__ == '__main__':
        pass


    
        





