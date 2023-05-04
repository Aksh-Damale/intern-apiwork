from fastapi import FastAPI
from app.routes.vehicle_type_route import vehicle_type_route
from app.routes.vehicle_manufacturer_route import vehicle_manufacturer_route
from app.routes.vehicle_model_route import vehicle_model_route
from app.routes.vehicle_variant_route import vehicle_variant_route
from app.routes.cluster_route import cluster_route
from app.routes.vehicle_cluster_route import vehicle_cluster_route
from app.routes.ecu_manufacturer_route import ecu_manufacturer_route
from app.routes.ecu_route import ecu_route
from app.routes.vehicle_cluster_ecu_route import vehicle_cluster_ecu_route
from app.routes.dashboard_route import dashboard_router
from app.routes.bom_route import bom_route

app = FastAPI(title="SecureThings Cyber Intel APIs", version="1.0")

ROOT_URL = "/secure-things/cyber_intel/api/v1"

app.include_router(dashboard_router, prefix=ROOT_URL, tags=["Dashboard"])
app.include_router(vehicle_type_route, prefix = ROOT_URL, tags = ["Vehicle Type"])
app.include_router(vehicle_manufacturer_route, prefix = ROOT_URL, tags = ["Vehicle Manufacturer"])
app.include_router(vehicle_model_route, prefix = ROOT_URL, tags = ["Vehicle Model"])
app.include_router(vehicle_variant_route, prefix = ROOT_URL, tags = ["Vehicle Variant"])
app.include_router(cluster_route, prefix = ROOT_URL, tags = ["Cluster"])
app.include_router(vehicle_cluster_route, prefix = ROOT_URL, tags = ["Vehicle Cluster"])
app.include_router(ecu_manufacturer_route, prefix = ROOT_URL, tags = ["ECU Manufacturer"])
app.include_router(ecu_route, prefix = ROOT_URL, tags = ["ECU"])
app.include_router(vehicle_cluster_ecu_route, prefix = ROOT_URL, tags = ["Vehicle Cluster ECU"])
app.include_router(bom_route, prefix = ROOT_URL, tags = ["Vehicle BOM"])