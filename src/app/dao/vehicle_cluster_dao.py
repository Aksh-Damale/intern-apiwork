from app.util import db_util
from app.dao.cyber_intel_dao import CyberIntelDao

class VehicleClusterDao:

    @classmethod
    def __get_vehicle_cluster_collection(cls):
        db = db_util.get_cyber_intel_mongodb_connection()
        return db["vehicle_clusters"]
    
    @staticmethod
    def insert_vehicle_cluster(cluster):
        collection = VehicleClusterDao.__get_vehicle_cluster_collection()
        print("Inserting Vehicle Cluster in Database...")
        res = CyberIntelDao.insert_data(collection, cluster)
        print("Vehicle Cluster Inserted Successfully")
        return res
    
    @staticmethod
    def get_cluster_connections_by_variant_id(variant_id):
        collection = VehicleClusterDao.__get_vehicle_cluster_collection()
        param = {"vehicle_variant_id": variant_id}
        columns = {"_id": 0, "clusters": 1, "cluster_connections": 1}
        return CyberIntelDao.get_data_by_params(collection, param, columns)
