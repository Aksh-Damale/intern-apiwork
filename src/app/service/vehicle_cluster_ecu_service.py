from app.service.vehicle_variant_service import VehicleVariantService
from app.service.cluster_service import ClusterService
from app.service.ecu_service import ECUService
from app.dao.vehicle_cluster_ecu_dao import VehicleClusterECUDao

class VehicleClusterECUService:

    @staticmethod
    def insert_vehicle_cluster_ecu(vehicle_cluster_ecu):
        vehicle_variant = VehicleVariantService.get_vehicle_variant_by_name(vehicle_cluster_ecu["vehicle_variant_id"]["vehicle_variant"])
        cluster = ClusterService.get_cluster_by_name(vehicle_cluster_ecu["cluster_id"]["cluster_name"])
        if vehicle_variant is not None and cluster is not None:
            vehicle_cluster_ecu["vehicle_variant_id"] = vehicle_variant[0]["_id"]
            vehicle_cluster_ecu["cluster_id"] = cluster[0]["_id"]
            ecu_presence = []
            for ecu in vehicle_cluster_ecu["ecus"]:
                if ECUService.get_ecu_by_name(ecu) is not None:
                    ecu_presence.append(True)
                else:
                    ecu_presence.append(False)
            if ecu_presence[0] and ecu_presence.count(ecu_presence[0]) == len(ecu_presence):
                return VehicleClusterECUDao.insert_vehicle_cluster_ecu(vehicle_cluster_ecu)
        return None

    @staticmethod
    def get_ecu_connections_by_variant(vehicle_variant, cluster):
        vehicle_variant = VehicleVariantService.get_vehicle_variant_by_name(vehicle_variant)
        cluster = ClusterService.get_cluster_by_name(cluster)
        if vehicle_variant is not None and cluster is not None:
            return VehicleClusterECUDao.get_ecu_connections_by_variant_and_cluster_id(vehicle_variant[0]["_id"], cluster[0]["_id"])
        return None
