from app.dao.cluster_dao import ClusterDao

class ClusterService:

    @staticmethod
    def insert_cluster(cluster):
        return ClusterDao.insert_cluster(cluster)
    
    @staticmethod
    def get_all_clusters():
        return ClusterDao.get_all_clusters()
    
    @staticmethod
    def get_cluster_by_name(name):
        return ClusterDao.get_cluster_by_name(name)