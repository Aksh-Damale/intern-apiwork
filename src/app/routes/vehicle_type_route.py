from fastapi import Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
from app.model.models import VehicleType
from app.service.vehicle_type_service import VehicleTypeService
from app.handler.response_handler import APIResponse

vehicle_type_route = APIRouter()

@vehicle_type_route.post("/add/vehicle/type", status_code = status.HTTP_201_CREATED, response_model=VehicleType)
async def add_vehicle_type(payload: VehicleType):
    res = VehicleTypeService.insert_vehicle_type(payload.dict())
    if res is not None:
        return JSONResponse(content=APIResponse("Created", status.HTTP_201_CREATED, payload).get_response(), status_code=201)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Vehicle Type Insert Failed")

@vehicle_type_route.get("/all/vehicle/types", status_code = status.HTTP_200_OK, response_model=List[VehicleType])
async def get_all_vehicle_types():
    vehicle_types = VehicleTypeService.get_all_vehicle_types()
    if vehicle_types is not None and len(vehicle_types) > 0:
        return JSONResponse(content=APIResponse("OK", status.HTTP_200_OK, vehicle_types).get_response(), status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle Types Not Found")