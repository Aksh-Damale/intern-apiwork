from app.util import db_util
from app.dao.cyber_intel_dao import CyberIntelDao

class VehicleVariantDao:

    @classmethod
    def __get_vehicle_variant_collection(cls):
        db = db_util.get_cyber_intel_mongodb_connection()
        return db["vehicle_variant"]
    
    @staticmethod
    def insert_vehicle_variant(vehicle_variant):
        collection = VehicleVariantDao.__get_vehicle_variant_collection()
        print("Inserting Vehicle Variant in Database...")
        res = CyberIntelDao.insert_data(collection, vehicle_variant)
        print("Vehicle Variant Inserted Successfully")
        return res
    
    @staticmethod
    def get_all_vehicle_variants_by_model(vehicle_model):
        collection = VehicleVariantDao.__get_vehicle_variant_collection()
        param = {"vehicle_model_id": vehicle_model}
        columns = {"_id": 0, "vehicle_variant": 1, "year_of_manufacturing": 1}
        return CyberIntelDao.get_data_by_params(collection, param, columns)
    
    @staticmethod
    def get_vehicle_variant_by_name(name):
        collection = VehicleVariantDao.__get_vehicle_variant_collection()
        param = {"vehicle_variant": name}
        return CyberIntelDao.get_data_by_params(collection, param)