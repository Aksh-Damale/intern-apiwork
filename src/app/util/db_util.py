import pymongo
from app.config.db_config import MONGODB_URI, CYBER_INTEL_DB

def get_cyber_intel_mongodb_connection():
    connection = pymongo.MongoClient(MONGODB_URI)
    return connection[CYBER_INTEL_DB]



if __name__ == "__main__":
   print(get_cyber_intel_mongodb_connection())