from fastapi import Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.model.models import ECUManufacturer
from app.handler.response_handler import APIResponse
from app.service.ecu_manufacturer_service import ECUManufacturerService

ecu_manufacturer_route = APIRouter()

@ecu_manufacturer_route.post("/add/ecu/manufacturer", status_code = status.HTTP_201_CREATED, response_model=ECUManufacturer)
async def add_ecu_manufacturer(payload: ECUManufacturer):
    res = ECUManufacturerService.insert_ecu_manufacturer(payload.dict())
    if res is not None:
        return JSONResponse(content=APIResponse("Created", status.HTTP_201_CREATED, payload).get_response(), status_code=201)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="ECU Manufacturer Insert Failed")
    
@ecu_manufacturer_route.get("/all/ecu/manufacturers", status_code = status.HTTP_200_OK)
async def get_all_ecu_manufacturers():
    ecu_manufacturers = ECUManufacturerService.get_all_ecu_manufacturers()
    if ecu_manufacturers is not None and len(ecu_manufacturers) > 0:
        return JSONResponse(content=APIResponse("OK", status.HTTP_200_OK, ecu_manufacturers).get_response(), status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ECU Manufacturers Not Found")