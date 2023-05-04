from app.dao.ecu_dao import ECUDao
from app.service.ecu_manufacturer_service import ECUManufacturerService

class ECUService:

    @staticmethod
    def insert_ecu(ecu):
        ecu_manufacturer = ECUManufacturerService.get_ecu_manufacturer_by_name(ecu["ecu_mfg_id"]["ecu_manufacturer"])
        if ecu_manufacturer is not None:
            ecu["ecu_mfg_id"] = ecu_manufacturer[0]["_id"]
            return ECUDao.insert_ecu(ecu)
        else:
            return None
    
    @staticmethod
    def get_all_ecus():
        ecus = ECUDao.get_all_ecus()
        for ecu in ecus:
            manufacturer = ECUManufacturerService.get_ecu_manufacturer_by_id(ecu["ecu_mfg_id"])
            if manufacturer is not None:
                ecu["ecu_mfg_id"] = manufacturer[0]["ecu_manufacturer"]
        return ecus

    @staticmethod
    def get_ecu_by_name(name):
        return ECUDao.get_ecu_by_name(name)