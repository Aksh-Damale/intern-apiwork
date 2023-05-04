from app.util import db_util
from app.dao.cyber_intel_dao import CyberIntelDao

class VehicleManufacturerDao:

    @classmethod
    def __get_vehicle_manufacturer_collection(cls):
        db = db_util.get_cyber_intel_mongodb_connection()
        return db["vehicle_manufacturer"]
    
    @staticmethod
    def insert_vehicle_manufacturer(vehicle_manufacturer):
        collection = VehicleManufacturerDao.__get_vehicle_manufacturer_collection()
        print("Inserting Vehicle Manufacturer in Database...")
        res = CyberIntelDao.insert_data(collection, vehicle_manufacturer)
        print("Vehicle Manufacturer Inserted Successfully")
        return res

    @staticmethod
    def get_all_vehicle_manufacturers():
        collection = VehicleManufacturerDao.__get_vehicle_manufacturer_collection()
        return CyberIntelDao.get_all_data(collection)
    
    @staticmethod
    def get_vehicle_manufacturer_by_name(name):
        collection = VehicleManufacturerDao.__get_vehicle_manufacturer_collection()
        return CyberIntelDao.get_data_by_params(collection, {"vehicle_manufacturer": name})