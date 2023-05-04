from fastapi import Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.model.models import VehicleClusterECU
from app.handler.response_handler import APIResponse
from app.service.vehicle_cluster_ecu_service import VehicleClusterECUService

vehicle_cluster_ecu_route = APIRouter()

@vehicle_cluster_ecu_route.post("/add/vehicle/cluster/ecu", status_code = status.HTTP_201_CREATED, response_model=VehicleClusterECU)
async def add_vehicle_cluster_ecu(payload: VehicleClusterECU):
    res = VehicleClusterECUService.insert_vehicle_cluster_ecu(payload.dict())
    if res is not None:
        return JSONResponse(content=APIResponse("Created", status.HTTP_201_CREATED, payload).get_response(), status_code=201)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Vehicle Cluster ECU Insert Failed")

@vehicle_cluster_ecu_route.get("/vehicle/cluster/ecu/connections", status_code = status.HTTP_200_OK)
async def get_ecu_connections_by_variant_and_cluster(vehicle_variant: str, cluster: str):
    ecu_connections = VehicleClusterECUService.get_ecu_connections_by_variant(vehicle_variant, cluster)
    if ecu_connections is not None:
        return JSONResponse(content=APIResponse("OK", status.HTTP_200_OK, ecu_connections).get_response(), status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="ECU Connections for the Variant: "+vehicle_variant+" & Cluster: "+cluster+" Not Found")