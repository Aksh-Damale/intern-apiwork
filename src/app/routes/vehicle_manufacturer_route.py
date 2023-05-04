from fastapi import Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
from app.model.models import VehicleManufacturer
from app.service.vehicle_manufacturer_service import VehicleManufacturerService
from app.handler.response_handler import APIResponse

vehicle_manufacturer_route = APIRouter()

@vehicle_manufacturer_route.post("/add/vehicle/manufacturer", status_code = status.HTTP_201_CREATED, response_model=VehicleManufacturer)
async def add_vehicle_manufacturer(payload: VehicleManufacturer):
    res = VehicleManufacturerService.insert_vehicle_manufacturer(payload.dict())
    if res is not None:
        return JSONResponse(content=APIResponse("Created", status.HTTP_201_CREATED, payload).get_response(), status_code=201)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Vehicle Manufacturer Insert Failed")

@vehicle_manufacturer_route.get("/all/vehicle/manufacturers", status_code = status.HTTP_200_OK, response_model=List[VehicleManufacturer])
async def get_all_vehicle_manufacturers():
    vehicle_types = VehicleManufacturerService.get_all_vehicle_manufacturers()
    if vehicle_types is not None and len(vehicle_types) > 0:
        return JSONResponse(content=APIResponse("OK", status.HTTP_200_OK, vehicle_types).get_response(), status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle Manufacturers Not Found")