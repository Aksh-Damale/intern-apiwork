from fastapi import Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.model.models import ECU
from app.handler.response_handler import APIResponse
from app.service.ecu_service import ECUService

ecu_route = APIRouter()

@ecu_route.post("/add/ecu", status_code = status.HTTP_201_CREATED, response_model=ECU)
async def add_ecu(payload: ECU):
    res = ECUService.insert_ecu(payload.dict())
    if res is not None:
        return JSONResponse(content=APIResponse("Created", status.HTTP_201_CREATED, payload).get_response(), status_code=201)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="ECU Insert Failed")

@ecu_route.get("/all/ecus", status_code = status.HTTP_200_OK)
async def get_all_ecus():
    ecus = ECUService.get_all_ecus()
    if ecus is not None and len(ecus) > 0:
        return JSONResponse(content=APIResponse("OK", status.HTTP_200_OK, ecus).get_response(), status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ECUs Not Found")