from typing import List
from fastapi import Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.model.models import VehicleModel
from app.handler.response_handler import APIResponse
from app.service.vehicle_model_service import VehicleModelService

vehicle_model_route = APIRouter()

@vehicle_model_route.post("/add/vehicle/model", status_code = status.HTTP_201_CREATED, response_model=VehicleModel)
async def add_vehicle_model(payload: VehicleModel):
    res = VehicleModelService.insert_vehicle_model(payload.dict())
    if res is not None:
        return JSONResponse(content=APIResponse("Created", status.HTTP_201_CREATED, payload).get_response(), status_code=201)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Vehicle Model Insert Failed")

@vehicle_model_route.get("/all/vehicle/models", status_code = status.HTTP_200_OK)
async def get_all_vehicle_models():
    vehicle_models = VehicleModelService.get_all_vehicle_models()
    if vehicle_models is not None and len(vehicle_models) > 0:
        return JSONResponse(content=APIResponse("OK", status.HTTP_200_OK, vehicle_models).get_response(), status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle Models Not Found")
