from entities.employee import Employee
from entities.updateEmployee import UpdateEmployee


def formatUpdateRTData(employee: Employee | list[Employee] | UpdateEmployee):
    data = {
        "mdmtaxid": employee.taxid,
        "employeecode": employee.employeecode,
        "mdmname": employee.name,
        "mdmpersonid": employee.personid,
        "mdmemailaddress": employee.email,
        "isterminated": employee.isterminated,
        "admissionaldate": employee.admissiondate,
        "mdmaddress": [
            # pegar info do geofence
        ],
    }

    return data
