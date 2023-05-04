from app.util import db_util
from app.dao.cyber_intel_dao import CyberIntelDao

class ECUManufacturerDao:

    @classmethod
    def __get_ecu_manufacturer_collection(cls):
        db = db_util.get_cyber_intel_mongodb_connection()
        return db["ecu_manufacturer"]
    
    @staticmethod
    def insert_ecu_manufacturer(ecu_manufacturer):
        collection = ECUManufacturerDao.__get_ecu_manufacturer_collection()
        print("Inserting ECU Manufacturer in Database...")
        res = CyberIntelDao.insert_data(collection, ecu_manufacturer)
        print("ECU Manufacturer Inserted Successfully")
        return res
    
    @staticmethod
    def get_all_ecu_manufacturers():
        collection = ECUManufacturerDao.__get_ecu_manufacturer_collection()
        return CyberIntelDao.get_all_data(collection)

    @staticmethod
    def get_ecu_manufacturer_by_id(id):
        collection = ECUManufacturerDao.__get_ecu_manufacturer_collection()
        param = {"_id": id}
        return CyberIntelDao.get_data_by_params(collection, param)

    @staticmethod
    def get_ecu_manufacturer_by_name(name):
        collection = ECUManufacturerDao.__get_ecu_manufacturer_collection()
        param = {"ecu_manufacturer": name}
        return CyberIntelDao.get_data_by_params(collection, param)