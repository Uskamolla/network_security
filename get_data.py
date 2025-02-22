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
        
    def csv2json(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)  
            records = list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def data2mongodb(self, records, database, collection):
        try:
            self.database = database 
            self.collection = collection 
            self.records = records 

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)

            return len(self.records)
        

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        


if __name__ == '__main__':
    FILE_PATH = r"D:\projects\network_security\Data\NetworkData.csv"
    DATABASE = "PersonalProject"
    COLLECTION = "NetworkData"
    network_data = dataextraction()
    records = network_data.csv2json(FILE_PATH)
    numrecords = network_data.data2mongodb(records, DATABASE, COLLECTION)
    print(numrecords)
        


    
        





