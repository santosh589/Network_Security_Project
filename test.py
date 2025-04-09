import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi   ## Its is a python package that provide set of root certificates, to make a secure connections. to verify trusted certified request made. 
ca = certifi.where( )

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def cv_to_json_convert(self,file_path):
        try:
            data= pd.read_csv(file_path)
            data.reset_index(drop= True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self, records,database, collection):
        try:
            self.database= database
            self.collection = collection
            self.records = records 

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__=='__main__':
    FILE_PATH = ('Network_data\phisingData.csv')
    DATABASE= "NETWORK_DB"
    COLLECTION = "NETWORK_DATA"
    networkobj= NetworkDataExtract()
    records =networkobj.cv_to_json_convert(file_path=FILE_PATH)
    print(records)
    no_of_records= networkobj.insert_data_mongodb(records, DATABASE, COLLECTION )
    print(no_of_records)






    


