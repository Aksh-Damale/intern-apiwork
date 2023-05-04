from typing import List
from fastapi import Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.model.models import VehicleVariant
from app.handler.response_handler import APIResponse
from app.service.vehicle_variant_service import VehicleVariantService

vehicle_variant_route = APIRouter()

@vehicle_variant_route.post("/add/vehicle/variant", status_code = status.HTTP_201_CREATED, response_model=VehicleVariant)
async def add_vehicle_variant(payload: VehicleVariant):
    res = VehicleVariantService.insert_vehicle_variant(payload.dict())
    if res is not None:
        return JSONResponse(content=APIResponse("Created", status.HTTP_201_CREATED, payload).get_response(), status_code=201)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Vehicle Variant Insert Failed")

@vehicle_variant_route.get("/all/vehicle/variants", status_code = status.HTTP_200_OK)
async def get_all_vehicle_variants_by_type_and_model(vehicle_type: str, vehicle_model: str):
    vehicle_variants = VehicleVariantService.get_all_vehicle_variants_by_type_and_model(vehicle_type, vehicle_model)
    if vehicle_variants is not None and len(vehicle_variants) > 0:
        return JSONResponse(content=APIResponse("OK", status.HTTP_200_OK, vehicle_variants).get_response(), status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle Variants Not Found")