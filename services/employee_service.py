from models import employee_model
from entities.employee import Employee
from entities.geofence import Geofence

from utils.formatEmployeeData import formatEmployeeData
from utils.formatGeofenceData import formatGeofenceData


async def createEmployee(employee: Employee | list[Employee]):
    dataToEmployeeStaging = formatEmployeeData(employee)
    dataToGeofenceStaging = formatGeofenceData(employee)

    return await employee_model.createEmployee(
        dataToEmployeeStaging, dataToGeofenceStaging
    )


async def addGeofence(employee: Geofence | list[Geofence]):
    dataToGeofenceStaging = formatGeofenceData(employee)

    return await employee_model.addGeofence(dataToGeofenceStaging)
