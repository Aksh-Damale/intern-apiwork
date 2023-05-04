from app.dao.vehicle_manufacturer_dao import VehicleManufacturerDao

class VehicleManufacturerService:

    @staticmethod
    def insert_vehicle_manufacturer(vehicle_manufacturer):
        return VehicleManufacturerDao.insert_vehicle_manufacturer(vehicle_manufacturer)
    
    @staticmethod
    def get_all_vehicle_manufacturers():
        return VehicleManufacturerDao.get_all_vehicle_manufacturers()
    
    @staticmethod
    def get_vehicle_manufacturer_by_name(name):
        return VehicleManufacturerDao.get_vehicle_manufacturer_by_name(name)