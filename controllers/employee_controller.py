from fastapi import APIRouter, HTTPException

from services import employee_service
from entities.employee import Employee
from entities.geofence import Geofence
from entities.updateEmployee import UpdateEmployee

router = APIRouter()


@router.get("/")
async def getAllEmployees():
    return await employee_service.getAllEmployees()


@router.get("/taxid/{taxId}/employeecode/{employeeCode}")
async def getByEmployeeCodeAndTaxId(taxId: str, employeeCode: str):
    response = await employee_service.getByEmployeeCodeAndTaxId(taxId, employeeCode)

    if len(response) == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    else:
        return response[0]


@router.get("/taxid/{taxId}")
async def getAllByTaxId(taxId: str):
    response = await employee_service.getAllByTaxId(taxId)

    if len(response) == 0:
        raise HTTPException(status_code=404, detail="Tax Id not found")
    else:
        return response


@router.post("/")
async def createEmployee(employee: Employee | list[Employee]):
    return await employee_service.createEmployee(employee)


@router.post("/geofence")
async def addGeofence(employee: Geofence | list[Geofence]):
    return await employee_service.addGeofence(employee)


@router.put("/taxid/{taxId}/employeecode/{employeeCode}")
async def updateEmployee(updateData: UpdateEmployee, taxId: str, employeeCode: str):
    updateData.taxid = taxId
    updateData.employeecode = employeeCode

    return await employee_service.updateEmployee(updateData)


@router.delete("/taxid/{taxId}/employeecode/{employeeCode}/id/{id}")
async def deleteEmployee(taxId: str, employeeCode: str, id: str):
    response = await employee_service.deleteEmployee(taxId, employeeCode, id)

    if response is False:
        raise HTTPException(
            status_code=404, detail="EmployeeCode or TaxId or ID not found"
        )
    else:
        return response
