from app.util import db_util
from app.dao.cyber_intel_dao import CyberIntelDao
from bson.objectid import ObjectId

class BOMDao:

    @classmethod
    def __get_bom_collection(cls):
        db = db_util.get_cyber_intel_mongodb_connection()
        return db["bom"]
    
    @staticmethod
    def insert_bom(bom):
        collection = BOMDao.__get_bom_collection()
        print("Inserting Vehicle BOM in Database...")
        res = CyberIntelDao.insert_data(collection, bom)
        print("Vehicle BOM Inserted Successfully")
        return res
    
    @staticmethod
    def get_bom_by_variant_ecu_and_version(vehicle_variant, ecu, version):
        collection = BOMDao.__get_bom_collection()
        match = {"$match": {"vehicle_variant_id": ObjectId(vehicle_variant), "ecu_id": ObjectId(ecu), "bom_version": version}}
        project = {"$project": {"_id":0,"hardware_details": {"$map": {'input': '$hardware_details', 'as': 'hwd', 'in': {'name': '$$hwd.hardware_bom', 'criticality': '$$hwd.criticality', 'current_status': '$$hwd.current_status'}}}, 'software_details': {'$map': {'input': '$software_details', 'as': 'sfw', 'in': {'packages': '$$sfw.packages'}}}}}
        param = [match, project]
        return CyberIntelDao.get_data_by_aggregate_func(collection, param)
    
    @staticmethod
    def get_bom_versions():
        collection = BOMDao.__get_bom_collection()
        param = [{'$group': {'_id': None, 'bom_version': {'$addToSet': '$bom_version'}}}]
        return CyberIntelDao.get_data_by_aggregate_func(collection, param)