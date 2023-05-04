from app.service.vehicle_model_service import VehicleModelService
from app.service.vehicle_type_service import VehicleTypeService
from app.dao.vehicle_variant_dao import VehicleVariantDao

class VehicleVariantService:

    @staticmethod
    def insert_vehicle_variant(vehicle_variant):
        vehicle_model = VehicleModelService.get_vehicle_model_by_name(vehicle_variant["vehicle_model_id"]["vehicle_model"])
        if vehicle_model is not None:
            vehicle_variant["vehicle_model_id"] = vehicle_model[0]["_id"]
            return VehicleVariantDao.insert_vehicle_variant(vehicle_variant)
        else:
            return None
    
    @staticmethod
    def get_all_vehicle_variants_by_type_and_model(vehicle_type, vehicle_model):
        vehicle_type = VehicleTypeService.get_vehicle_type_by_type(vehicle_type)
        if vehicle_type is not None:
            vehicle_model = VehicleModelService.get_vehicle_model_by_type_and_model(vehicle_type[0]["_id"], vehicle_model)
            if vehicle_model is not None:
                return VehicleVariantDao.get_all_vehicle_variants_by_model(vehicle_model[0]["_id"])
        return None
    
    @staticmethod
    def get_vehicle_variant_by_name(name):
        return VehicleVariantDao.get_vehicle_variant_by_name(name)