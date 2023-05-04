from app.service.vehicle_variant_service import VehicleVariantService
from app.service.ecu_service import ECUService
from app.dao.bom_dao import BOMDao

class BOMService:

    @staticmethod
    def insert_vehicle_bom(bom):
        vehicle_variant = VehicleVariantService.get_vehicle_variant_by_name(bom["vehicle_variant_id"]["vehicle_variant"])
        ecu = ECUService.get_ecu_by_name(bom["ecu_id"]["ecu_name"])
        if vehicle_variant is not None and ecu is not None:
            bom["vehicle_variant_id"] = vehicle_variant[0]["_id"]
            bom["ecu_id"] = ecu[0]["_id"]
            return BOMDao.insert_bom(bom)
        return None
    
    @staticmethod
    def get_bom_by_variant_ecu_and_version(vehicle_variant, ecu, version):
        vehicle_variant = VehicleVariantService.get_vehicle_variant_by_name(vehicle_variant)
        ecu = ECUService.get_ecu_by_name(ecu)
        if vehicle_variant is not None and ecu is not None:
            bom = BOMDao.get_bom_by_variant_ecu_and_version(vehicle_variant[0]["_id"], ecu[0]["_id"], version)
            packages = []
            for software in bom[0]["software_details"]:
                for package in software["packages"]:
                    if package["package_name"] is not None and package["package_name"] != "":
                        final_package = {}
                        final_package["name"] = package["package_name"]
                        final_package["criticality"] = package["criticality"]
                        final_package["current_status"] = package["current_status"]
                        packages.append(final_package)
            bom[0]["software_details"] = packages
            return bom
        return None
    
    @staticmethod
    def get_bom_versions():
        versions = BOMDao.get_bom_versions()
        return versions[0]["bom_version"]