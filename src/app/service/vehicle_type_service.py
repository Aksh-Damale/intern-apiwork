from app.dao.vehicle_type_dao import VehicleTypeDao

class VehicleTypeService:

    @staticmethod
    def insert_vehicle_type(vehicle_type):
        return VehicleTypeDao.insert_vehicle_type(vehicle_type)
    
    @staticmethod
    def get_all_vehicle_types():
        return VehicleTypeDao.get_all_vehicle_types()
    
    @staticmethod
    def get_vehicle_type_by_type(vehicle_type):
        return VehicleTypeDao.get_vehicle_type_by_type(vehicle_type)