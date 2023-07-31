from fastapi import APIRouter

from services import employee_service
from entities.employee import Employee
from entities.geofence import Geofence

router = APIRouter()


@router.get("/")
async def getAllEmployees():
    return {"employees": "all"}


@router.post("/")
async def createEmployee(employee: Employee | list[Employee]):
    return await employee_service.createEmployee(employee)


@router.post("/geofence")
async def addGeofence(employee: Geofence | list[Geofence]):
    return await employee_service.addGeofence(employee)
