from fastapi import Header, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.model.models import Dashboard, ResponseValue
from app.handler.response_handler import APIResponse

dashboard_router = APIRouter()

dashbordobj = Dashboard()


@dashboard_router.get("/toal_vul_vehicle_count", status_code=status.HTTP_200_OK)
async def get_total_vul_vehicle_count(oem: str):
    return ResponseValue(
        response_code=status.HTTP_200_OK,
        response_value={
            "total_vul_vehicle_count": dashbordobj.total_vul_vehicle},
    )


@dashboard_router.get("/owasp_exploits_count", status_code=status.HTTP_200_OK)
async def get_oem_exploits_count(oem: str):
    return ResponseValue(
        response_code=status.HTTP_200_OK,
        response_value={
            "owasp_exploits_count": dashbordobj.owasp_exploits_count,
        }
    )


@dashboard_router.get("/oemwise_vehicle_hackability", status_code=status.HTTP_200_OK)
async def get_oemwise_vehicle_hackability():
    return ResponseValue(
        response_code=status.HTTP_200_OK,
        response_value={
            "oemwise_vehicle_hackability": dashbordobj.oemwise_vehicle_hackability,
        }
    )


@dashboard_router.get("/affected_clusters", status_code=status.HTTP_200_OK)
async def get_variantwise_affected_cluster_rating(oem: str):
    return ResponseValue(
        response_code=status.HTTP_200_OK,
        response_value={
            "variant_affected_cluster": dashbordobj.variant_affected_clusters}
    )


@dashboard_router.get('/ECU_21434_compliance_rating')
async def get_cariant_wise_ecu_compliance_rating(oem: str):
    return ResponseValue(
        response_code=status.HTTP_200_OK,
        response_value={
            "ecu_21434_compliance_rating": dashbordobj.ecu_21434_compliance_rating}
    )
    
    
@dashboard_router.get("/vendor_wise_vulnerability_count", status_code=status.HTTP_200_OK)
async def get_vendorwise_vul_hackability(oem: str):
    return ResponseValue(
        response_code=status.HTTP_200_OK,
        response_value={
            "vendor_vul_count" : dashbordobj.vendor_vul_count
        }
    )
    
@dashboard_router.get("/vendor_wise_avg_severity", status_code=status.HTTP_200_OK)
async def get_vendor_wise_avg_severity(oem: str):
    return ResponseValue(
        response_code=status.HTTP_200_OK,
        response_value={
            "vendor_wise_comparision": dashbordobj.vendor_wise_comparision
        }
    )
