from app.util import db_util
from app.dao.cyber_intel_dao import CyberIntelDao

class ClusterDao:

    @classmethod
    def __get_cluster_collection(cls):
        db = db_util.get_cyber_intel_mongodb_connection()
        return db["cluster"]
    
    @staticmethod
    def insert_cluster(cluster):
        collection = ClusterDao.__get_cluster_collection()
        print("Inserting Cluster in Database...")
        res = CyberIntelDao.insert_data(collection, cluster)
        print("Cluster Inserted Successfully")
        return res
    
    @staticmethod
    def get_all_clusters():
        collection = ClusterDao.__get_cluster_collection()
        return CyberIntelDao.get_all_data(collection)
    
    @staticmethod
    def get_cluster_by_name(name):
        collection = ClusterDao.__get_cluster_collection()
        param = {"cluster_name": name}
        return CyberIntelDao.get_data_by_params(collection, param)