from app.util import db_util
from app.dao.cyber_intel_dao import CyberIntelDao

class VehicleClusterECUDao:

    @classmethod
    def __get_vehicle_cluster_ecu_collection(cls):
        db = db_util.get_cyber_intel_mongodb_connection()
        return db["vehicle_cluster_ecus"]
    
    @staticmethod
    def insert_vehicle_cluster_ecu(vehicle_cluster_ecu):
        collection = VehicleClusterECUDao.__get_vehicle_cluster_ecu_collection()
        print("Inserting Vehicle Cluster ECU in Database...")
        res = CyberIntelDao.insert_data(collection, vehicle_cluster_ecu)
        print("Vehicle Cluster ECU Inserted Successfully")
        return res
    
    @staticmethod
    def get_ecu_connections_by_variant_and_cluster_id(variant_id, cluster_id):
        collection = VehicleClusterECUDao.__get_vehicle_cluster_ecu_collection()
        param = {"vehicle_variant_id": variant_id, "cluster_id": cluster_id}
        columns = {"_id": 0, "ecus": 1, "ecu_connections": 1}
        return CyberIntelDao.get_data_by_params(collection, param, columns)