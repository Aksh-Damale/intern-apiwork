from app.util import db_util
from app.dao.cyber_intel_dao import CyberIntelDao

class VehicleTypeDao:

    @classmethod
    def __get_vehicle_type_collection(cls):
        db = db_util.get_cyber_intel_mongodb_connection()
        return db["vehicle_type"]

    @staticmethod
    def upsert_vehicle_type(vehicle_type):
        collection = VehicleTypeDao.__get_vehicle_type_collection()
        vehicle_types = VehicleTypeDao.get_all_vehicle_types()
        if vehicle_types is not None and len(vehicle_types) > 0:
            print("Upserting Vehicle Type in Database...")
            print("Upsert of Vehicle Type in Database Completed")
        else:
            print("Inserting Vehicle Type in Database...")
            collection.insert_many(vehicle_type)
            print("Vehicle Type Inserted Successfully")
    
    @staticmethod
    def insert_vehicle_type(vehicle_type):
        collection = VehicleTypeDao.__get_vehicle_type_collection()
        print("Inserting Vehicle Type in Database...")
        res = CyberIntelDao.insert_data(collection, vehicle_type)
        print("Vehicle Type Inserted Successfully")
        return res

    @staticmethod
    def get_all_vehicle_types():
        collection = VehicleTypeDao.__get_vehicle_type_collection()
        return CyberIntelDao.get_all_data(collection)
    
    @staticmethod
    def get_vehicle_type_by_type(vehicle_type):
        collection = VehicleTypeDao.__get_vehicle_type_collection()
        return CyberIntelDao.get_data_by_params(collection, {"vehicle_type": vehicle_type})