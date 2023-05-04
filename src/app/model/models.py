from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


class VehicleType(BaseModel):
    vehicle_type: str
    parent_type: str
    created_date: datetime = datetime.now()
    last_modified_date: datetime = datetime.now()


class VehicleManufacturer(BaseModel):
    vehicle_manufacturer: str
    created_date: datetime = datetime.now()
    last_modified_date: datetime = datetime.now()


class VehicleModel(BaseModel):
    vehicle_model: str
    vehicle_type_id: VehicleType
    vehicle_manufacturer_id: VehicleManufacturer
    created_date: datetime = datetime.now()
    last_modified_date: datetime = datetime.now()


class VehicleVariant(BaseModel):
    vehicle_variant: str
    year_of_manufacturing: int
    vehicle_model_id: VehicleModel
    vulnerable: bool
    threat_score: str
    ecu_level: str
    vehicle_severity: str
    created_date: datetime = datetime.now()
    last_modified_date: datetime = datetime.now()


class Cluster(BaseModel):
    cluster_name: str
    short_name: str
    cluster_function: str
    created_date: datetime = datetime.now()
    last_modified_date: datetime = datetime.now()


class ClusterConnections(BaseModel):
    source_cluster: str
    target_cluster: str
    connection_interfaces: List[str]


class VehicleCluster(BaseModel):
    vehicle_variant_id: VehicleVariant
    number_of_clusters: int
    clusters: List[str]
    cluster_connections: List[ClusterConnections]
    created_date: datetime = datetime.now()
    last_modified_date: datetime = datetime.now()


class ECUManufacturer(BaseModel):
    ecu_manufacturer: str
    created_date: datetime = datetime.now()
    last_modified_date: datetime = datetime.now()


class ECU(BaseModel):
    ecu_name: str
    short_name: str
    ecu_function: str
    ecu_mfg_id: ECUManufacturer
    endpoint_or_gateway: str
    created_date: datetime = datetime.now()
    last_modified_date: datetime = datetime.now()


class IntraClusterConnections(BaseModel):
    source_ecu: str
    target_ecu: str
    connection_interfaces: List[str]


class InterClusterConnections(BaseModel):
    source_ecu: str
    target_cluster: str
    connection_interfaces: List[str]


class ECUConnections(BaseModel):
    intra_cluster_connections: List[IntraClusterConnections]
    inter_cluster_connections: List[InterClusterConnections]


class VehicleClusterECU(BaseModel):
    vehicle_variant_id: VehicleVariant
    cluster_id: Cluster
    number_of_ecus: int
    ecus: List[str]
    ecu_connections: ECUConnections
    created_date: datetime = datetime.now()
    last_modified_date: datetime = datetime.now()


class Connections(BaseModel):
    component: str
    connection_interface: str


class HardwareDetails(BaseModel):
    hardware_bom: str
    component_id: str
    description: str
    component_type: str
    manufacturer: str
    architecture: str
    word_size: int
    pcb_id: str
    part_number: str
    total_local_interfaces: str
    connections: List[Connections]
    total_external_interfaces: str
    criticality: str
    current_status: str


class Package(BaseModel):
    package_name: str
    package_actual_name: str
    package_version: str
    package_type: str
    package_category: str
    package_path: str
    dependent_libs: List[str]
    application_type: str
    criticality: str
    current_status: str


class SoftwareDetails(BaseModel):
    hardware_bom: str
    component_type: str
    hardware_component_id: str
    system_type: str
    software_category: str
    packages: List[Package]


class BOM(BaseModel):
    vehicle_variant_id: VehicleVariant
    ecu_id: ECU
    bom_version: str
    hardware_details: List[HardwareDetails]
    software_details: List[SoftwareDetails]
    created_date: datetime = datetime.now()
    last_modified_date: datetime = datetime.now()


class OWASPExploitCountObj(BaseModel):
    vulnerability_name: str
    vulnerability_count: int


class OEMVehicleHackScoreObj(BaseModel):
    oem_name: str
    vehicle_hackability: float
    vulnerability_name: str
    vulnerability_count: int


class VariantAffectedClusterObj(BaseModel):
    variant_name: str
    most_affected_cluster: str
    cluster_rating: float


class ECUComplianceRatingObj(BaseModel):
    variant_name: str
    ecu_name: str
    vendor_name: str
    compliance_rating: str


class VendorVulCountObj(BaseModel):
    vendor_name: str
    vulnerabilities: int
    severities: List[Dict]
    
class VendorWiseCompObj(BaseModel):
    vendor_name: str
    vulnerabilities: int
    most_vulnerable_ecu : str
    hackability_score : float
    avg_severity : float


class Dashboard(BaseModel):
    total_vul_vehicle: int = Field(default=1304)
    owasp_exploits_count: List[OWASPExploitCountObj] = Field(
        default=[
            OWASPExploitCountObj(
                vulnerability_name="Vulnerable & Outdated Components",
                vulnerability_count=54
            ),
            OWASPExploitCountObj(
                vulnerability_name="Security Misconfigurations",
                vulnerability_count=45
            ),
            OWASPExploitCountObj(
                vulnerability_name="Injection",
                vulnerability_count=37
            ),
            OWASPExploitCountObj(
                vulnerability_name="Software & Data Integrity Failure",
                vulnerability_count=20
            ),
            OWASPExploitCountObj(
                vulnerability_name="Broken Access Control",
                vulnerability_count=14
            )
        ]
    )
    oemwise_vehicle_hackability: List[OEMVehicleHackScoreObj] = Field(
        default=[
            OEMVehicleHackScoreObj(
                oem_name="Tux",
                vehicle_hackability=0.32,
                vulnerability_name="Buffer Overflow",
                vulnerability_count=127
            ),
            OEMVehicleHackScoreObj(
                oem_name="Rev",
                vehicle_hackability=0.25,
                vulnerability_name="Vulnerable & Outdated Components",
                vulnerability_count=631
            ),
            OEMVehicleHackScoreObj(
                oem_name="Kif",
                vehicle_hackability=0.15,
                vulnerability_name="Vulnerable & Outdated Components",
                vulnerability_count=225
            )
        ]
    )
    variant_affected_clusters: List[VariantAffectedClusterObj] = Field(
        default=[
            VariantAffectedClusterObj(
                variant_name="Thunderbolt",
                most_affected_cluster="Digital Cockpit",
                cluster_rating=0.63,
            ),
            VariantAffectedClusterObj(
                variant_name="Twister",
                most_affected_cluster="Digital Cockpit",
                cluster_rating=0.63
            ),
            VariantAffectedClusterObj(
                variant_name="Ludo",
                most_affected_cluster="Digital Cockpit",
                cluster_rating=0.14
            )
        ]
    )
    ecu_21434_compliance_rating: List[ECUComplianceRatingObj] = Field(
        default=[
            ECUComplianceRatingObj(
                variant_name="Thunderbolt",
                ecu_name="IVI",
                vendor_name="isij",
                compliance_rating="low"
            ),
            ECUComplianceRatingObj(
                variant_name="Twister",
                ecu_name="CGW",
                vendor_name="4Q",
                compliance_rating="satisfactory",
            ),
            ECUComplianceRatingObj(
                variant_name="Ludo",
                ecu_name="TCU",
                vendor_name="CC",
                compliance_rating="Good",
            )

        ]
    )
    vendor_vul_count: List[VendorVulCountObj] = Field(
        default=[
            VendorVulCountObj(
                vendor_name="Tux",
                vulnerabilities=60,
                severities=[
                    {
                        "Severity": "Low",
                        "count": 20
                    },
                    {
                        "Severity": "Medium",
                        "count": 25,
                    },
                    {
                        "Severity": "High",
                        "count": 35,
                    },
                    {
                        "Severity": "Critical",
                        "count": 10
                    }
                ]
            ),
            VendorVulCountObj(
                vendor_name="Rev",
                vulnerabilities=40,
                severities=[
                    {
                        "Severity": "Low",
                        "count": 10
                    },
                    {
                        "Severity": "Medium",
                        "count": 30,
                    },
                    {
                        "Severity": "High",
                        "count": 12,
                    },
                    {
                        "Severity": "Critical",
                        "count": 25
                    }
                ]
            ),
            VendorVulCountObj(
                vendor_name="Kif",
                vulnerabilities=50,
                severities=[
                    [
                        {
                            "Severity": "Low",
                            "count": 13
                        },
                        {
                            "Severity": "Medium",
                            "count": 20,
                        },
                        {
                            "Severity": "High",
                            "count": 25,
                        },
                        {
                            "Severity": "Critical",
                            "count": 20
                        }
                    ],
                ]
            ),
            VendorVulCountObj(
                vendor_name="BM",
                vulnerabilities= 80,
                severities = [
                {
                    "Severity": "Low",
                    "count": 30
                },
                {
                    "Severity": "Medium",
                    "count": 40,
                },
                {
                    "Severity": "High",
                    "count": 35,
                },
                {
                    "Severity": "Critical",
                    "count": 30
                }
            ],
            ),
            VendorVulCountObj(
                vendor_name = "Lyn",
                vulnerabilities = 12,
                severities =  [
                {
                    "Severity": "Low",
                    "count": 3
                },
                {
                    "Severity": "Medium",
                    "count": 10,
                },
                {
                    "Severity": "High",
                    "count": 7,
                },
                {
                    "Severity": "Critical",
                    "count": 5
                }
            ],
            )
        ]
    )
    vendor_wise_comparision : List[VendorWiseCompObj] = Field(
        default= [
            VendorWiseCompObj(
                vendor_name = "Tux",
                vulnerabilities = 60,
                most_vulnerable_ecu = "IVI",
                hackability_score = 0.42,
                avg_severity = 3.25
            ),
            VendorWiseCompObj(
                vendor_name = "Rev",
                vulnerabilities = 40,
                most_vulnerable_ecu = "IVI",
                hackability_score = 0.32,
                avg_severity = 2.45  
            ),
            VendorWiseCompObj(
                vendor_name = "Kif",
                vulnerabilities = 50,
                most_vulnerable_ecu = "TCU",
                hackability_score = 0.25,
                avg_severity = 1.5
            ),
            VendorWiseCompObj(
                vendor_name = "BM",
                vulnerabilities = 80,
                most_vulnerable_ecu = "TCU",
                hackability_score = 0.15,
                avg_severity = 5.5
            ),
            VendorWiseCompObj(
                vendor_name = "Lyn",
                vulnerabilities = 12,
                most_vulnerable_ecu = "Engine ECU",
                hackability_score = 0.05,
                avg_severity = 1.5
            )
        ]
    
        
    )
class ResponseValue(BaseModel):
    response_code : int
    response_value : Dict[str, Any]
    response_message: str = Field(default='OK')