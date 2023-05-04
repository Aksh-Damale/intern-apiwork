from app.dao.ecu_manufacturer_dao import ECUManufacturerDao

class ECUManufacturerService:

    @staticmethod
    def insert_ecu_manufacturer(ecu_manufacturer):
        return ECUManufacturerDao.insert_ecu_manufacturer(ecu_manufacturer)
    
    @staticmethod
    def get_all_ecu_manufacturers():
        return ECUManufacturerDao.get_all_ecu_manufacturers()
    
    @staticmethod
    def get_ecu_manufacturer_by_id(id):
        return ECUManufacturerDao.get_ecu_manufacturer_by_id(id)

    @staticmethod
    def get_ecu_manufacturer_by_name(name):
        return ECUManufacturerDao.get_ecu_manufacturer_by_name(name)
