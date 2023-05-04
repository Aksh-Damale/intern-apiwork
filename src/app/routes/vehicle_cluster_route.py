from fastapi import Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.model.models import VehicleCluster
from app.handler.response_handler import APIResponse
from app.service.vehicle_cluster_service import VehicleClusterService

vehicle_cluster_route = APIRouter()

@vehicle_cluster_route.post("/add/vehicle/cluster", status_code = status.HTTP_201_CREATED, response_model=VehicleCluster)
async def add_vehicle_cluster(payload: VehicleCluster):
    res = VehicleClusterService.insert_vehicle_cluster(payload.dict())
    if res is not None:
        return JSONResponse(content=APIResponse("Created", status.HTTP_201_CREATED, payload).get_response(), status_code=201)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Vehicle Cluster Insert Failed")

@vehicle_cluster_route.get("/vehicle/cluster/connections", status_code = status.HTTP_200_OK)
async def get_cluster_connections_by_variant(vehicle_variant: str):
    cluster_connections = VehicleClusterService.get_cluster_connections_by_variant(vehicle_variant)
    if cluster_connections is not None:
        return JSONResponse(content=APIResponse("OK", status.HTTP_200_OK, cluster_connections).get_response(), status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cluster Connections for the Variant: "+vehicle_variant+" Not Found")