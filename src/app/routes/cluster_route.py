from fastapi import Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.model.models import Cluster
from app.handler.response_handler import APIResponse
from app.service.cluster_service import ClusterService

cluster_route = APIRouter()

@cluster_route.post("/add/cluster", status_code = status.HTTP_201_CREATED, response_model=Cluster)
async def add_cluster(payload: Cluster):
    res = ClusterService.insert_cluster(payload.dict())
    if res is not None:
        return JSONResponse(content=APIResponse("Created", status.HTTP_201_CREATED, payload).get_response(), status_code=201)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cluster Insert Failed")

@cluster_route.get("/all/clusters", status_code = status.HTTP_200_OK)
async def get_all_clusters():
    clusters = ClusterService.get_all_clusters()
    if clusters is not None and len(clusters) > 0:
        return JSONResponse(content=APIResponse("OK", status.HTTP_200_OK, clusters).get_response(), status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Clusters Not Found")