from app.util import db_util
from app.dao.cyber_intel_dao import CyberIntelDao

class ECUDao:

    @classmethod
    def __get_ecu_collection(cls):
        db = db_util.get_cyber_intel_mongodb_connection()
        return db["ecu"]
    
    @staticmethod
    def insert_ecu(ecu):
        collection = ECUDao.__get_ecu_collection()
        print("Inserting ECU in Database...")
        res = CyberIntelDao.insert_data(collection, ecu)
        print("ECU Inserted Successfully")
        return res
    
    @staticmethod
    def get_all_ecus():
        collection = ECUDao.__get_ecu_collection()
        return CyberIntelDao.get_all_data(collection)
    
    @staticmethod
    def get_ecu_by_name(name):
        collection = ECUDao.__get_ecu_collection()
        param = {"ecu_name": name}
        return CyberIntelDao.get_data_by_params(collection, param)