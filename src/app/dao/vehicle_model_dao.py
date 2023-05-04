from app.util import db_util
from app.dao.cyber_intel_dao import CyberIntelDao

class VehicleModelDao:

    @classmethod
    def __get_vehicle_model_collection(cls):
        db = db_util.get_cyber_intel_mongodb_connection()
        return db["vehicle_model"]
    
    @staticmethod
    def insert_vehicle_model(vehicle_model):
        collection = VehicleModelDao.__get_vehicle_model_collection()
        print("Inserting Vehicle Model in Database...")
        res = CyberIntelDao.insert_data(collection, vehicle_model)
        print("Vehicle Model Inserted Successfully")
        return res

    @staticmethod
    def get_all_vehicle_models():
        collection = VehicleModelDao.__get_vehicle_model_collection()
        manufacturer_lookup = {'$lookup': {'from': 'vehicle_manufacturer', 'localField': 'vehicle_manufacturer_id', 'foreignField': '_id', 'as': 'manufacturer'}}
        type_lookup = {'$lookup': {'from': 'vehicle_type', 'localField': 'vehicle_type_id', 'foreignField': '_id', 'as': 'type'}}
        project = {"$project": {"_id":0, "vehicle_model": 1, "manufacturer": 1, "type": 1, "manufacturer": {"$map": {"input": "$manufacturer", "as": "manu", "in": {"vehicle_manufacturer": "$$manu.vehicle_manufacturer"}}}, "type": {"$map": {"input": "$type", "as": "type", "in": {"vehicle_type": "$$type.vehicle_type"}}}}}
        param = [manufacturer_lookup, type_lookup, project]
        return CyberIntelDao.get_data_by_aggregate_func(collection, param)
    
    @staticmethod
    def get_vehicle_model_by_name(name):
        collection = VehicleModelDao.__get_vehicle_model_collection()
        param = {"vehicle_model": name}
        return CyberIntelDao.get_data_by_params(collection, param)
    
    @staticmethod
    def get_vehicle_model_by_type_and_model(vehicle_type, vehicle_model):
        collection = VehicleModelDao.__get_vehicle_model_collection()
        param = {"vehicle_type_id": vehicle_type,"vehicle_model": vehicle_model}
        return CyberIntelDao.get_data_by_params(collection, param)