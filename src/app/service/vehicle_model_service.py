from app.service.vehicle_manufacturer_service import VehicleManufacturerService
from app.service.vehicle_type_service import VehicleTypeService
from app.dao.vehicle_model_dao import VehicleModelDao

class VehicleModelService:

    @staticmethod
    def insert_vehicle_model(vehicle_model):
        vehicle_type = VehicleTypeService.get_vehicle_type_by_type(vehicle_model["vehicle_type_id"]["vehicle_type"])
        vehicle_manufacturer = VehicleManufacturerService.get_vehicle_manufacturer_by_name(vehicle_model["vehicle_manufacturer_id"]["vehicle_manufacturer"])
        if vehicle_type is not None and vehicle_manufacturer is not None:
            vehicle_model["vehicle_type_id"] = vehicle_type[0]["_id"]
            vehicle_model["vehicle_manufacturer_id"] = vehicle_manufacturer[0]["_id"]
            return VehicleModelDao.insert_vehicle_model(vehicle_model)
        else:
            return None
    
    @staticmethod
    def get_all_vehicle_models():
        return VehicleModelDao.get_all_vehicle_models()

    @staticmethod
    def get_vehicle_model_by_name(name):
        return VehicleModelDao.get_vehicle_model_by_name(name)

    @staticmethod
    def get_vehicle_model_by_type_and_model(vehicle_type, vehicle_model):
        return VehicleModelDao.get_vehicle_model_by_type_and_model(vehicle_type, vehicle_model)