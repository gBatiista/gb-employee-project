from models import employee_model
from entities.employee import Employee
from entities.geofence import Geofence
from entities.updateEmployee import UpdateEmployee

from utils.formatEmployeeData import formatEmployeeData
from utils.formatGeofenceData import formatGeofenceData
from utils.formatEmployeeRTData import formatEmployeeRTData
from utils.formatUpdateRTData import formatUpdateRTData


async def getAllEmployees():
    return await employee_model.getAllEmployees()


async def getByEmployeeCodeAndTaxId(taxId, employeeCode):
    return await employee_model.getByEmployeeCodeAndTaxId(taxId, employeeCode)


async def getAllByTaxId(taxId):
    return await employee_model.getAllByTaxId(taxId)


async def createEmployee(employee: Employee | list[Employee]):
    dataToEmployeeStg = formatEmployeeData(employee)
    dataToGeofenceStg = formatGeofenceData(employee)

    dataToRT = formatEmployeeRTData(employee)

    return await employee_model.createEmployee(
        dataToEmployeeStg, dataToGeofenceStg, dataToRT
    )


async def addGeofence(employee: Geofence | list[Geofence]):
    dataToGeofenceStaging = formatGeofenceData(employee)

    return await employee_model.addGeofence(dataToGeofenceStaging)


async def updateEmployee(dataToUpdate: UpdateEmployee):
    dataToEmployeeStg = formatEmployeeData(dataToUpdate)
    dataToRT = formatUpdateRTData(dataToUpdate)

    return await employee_model.updateEmployee(dataToEmployeeStg, dataToRT)


async def deleteEmployee(taxId: str, employeeCode: str, id: str):
    return await employee_model.deleteEmployee(taxId, employeeCode, id)
