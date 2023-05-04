from fastapi import Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.model.models import BOM
from app.handler.response_handler import APIResponse
from app.service.bom_service import BOMService

bom_route = APIRouter()

@bom_route.post("/add/bom", status_code = status.HTTP_201_CREATED, response_model=BOM)
async def add_bom(payload: BOM):
    res = BOMService.insert_vehicle_bom(payload.dict())
    if res is not None:
        return JSONResponse(content=APIResponse("Created", status.HTTP_201_CREATED, payload).get_response(), status_code=201)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Vehicle BOM Insert Failed")

@bom_route.get("/vehicle/bom", status_code = status.HTTP_200_OK)
async def get_bom_by_variant_ecu_and_version(vehicle_variant: str, ecu: str, version: str):
    bom_details = BOMService.get_bom_by_variant_ecu_and_version(vehicle_variant, ecu, version)
    if bom_details is not None:
        return JSONResponse(content=APIResponse("OK", status.HTTP_200_OK, bom_details).get_response(), status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="BOM Details of the Variant: "+vehicle_variant+", ECU: "+ecu+" & Version: "+version+" Not Found")

@bom_route.get("/vehicle/bom/versions", status_code = status.HTTP_200_OK)
async def get_bom_versions():
    versions = BOMService.get_bom_versions()
    if versions is not None:
        return JSONResponse(content=APIResponse("OK", status.HTTP_200_OK, versions).get_response(), status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="BOM Versions Not Found")