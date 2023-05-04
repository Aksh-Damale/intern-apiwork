from app.service.vehicle_variant_service import VehicleVariantService
from app.service.cluster_service import ClusterService
from app.dao.vehicle_cluster_dao import VehicleClusterDao

class VehicleClusterService:

    @staticmethod
    def insert_vehicle_cluster(vehicle_cluster):
        vehicle_variant = VehicleVariantService.get_vehicle_variant_by_name(vehicle_cluster["vehicle_variant_id"]["vehicle_variant"])
        if vehicle_variant is not None:
            vehicle_cluster["vehicle_variant_id"] = vehicle_variant[0]["_id"]
            cluster_presence = []
            for connection in vehicle_cluster["cluster_connections"]:
                source_cluster = ClusterService.get_cluster_by_name(connection["source_cluster"])
                target_cluster = ClusterService.get_cluster_by_name(connection["target_cluster"])
                if source_cluster is not None and target_cluster is not None:
                    cluster_presence.append(True)
                else:
                    cluster_presence.append(False)
            if cluster_presence[0] and cluster_presence.count(cluster_presence[0]) == len(cluster_presence):
                return VehicleClusterDao.insert_vehicle_cluster(vehicle_cluster)
            else:
                return None
        else:
            return None
    
    @staticmethod
    def get_cluster_connections_by_variant(vehicle_variant):
        vehicle_variant = VehicleVariantService.get_vehicle_variant_by_name(vehicle_variant)
        if vehicle_variant is not None:
            return VehicleClusterDao.get_cluster_connections_by_variant_id(vehicle_variant[0]["_id"])
        return None