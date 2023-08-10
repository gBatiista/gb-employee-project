from entities.employee import Employee
from entities.updateEmployee import UpdateEmployee


def formatEmployeeRTData(employee: Employee | list[Employee] | UpdateEmployee):
    data = None

    if type(employee) == list:
        data = [
            {
                "mdmtaxid": item.taxid,
                "employeecode": item.employeecode,
                "mdmname": item.name,
                "mdmpersonid": item.personid,
                "mdmemailaddress": item.email,
                "isterminated": item.isterminated,
                "admissionaldate": item.admissiondate,
                "mdmaddress": [
                    {
                        "mdmaddress1": item.address1,
                        "mdmaddress2": item.address2,
                        "mdmaddress3": item.address3,
                        "mdmcountry": item.country,
                        "mdmstate": item.state,
                        "mdmcity": item.city,
                        "mdmzipcode": item.zipcode,
                        "mdmaddresstype": item.type,
                        "gmt": item.gmt,
                    }
                ],
            }
            for item in employee
        ]

    else:
        data = {
            "mdmtaxid": employee.taxid,
            "employeecode": employee.employeecode,
            "mdmname": employee.name,
            "mdmpersonid": employee.personid,
            "mdmemailaddress": employee.email,
            "isterminated": employee.isterminated,
            "admissionaldate": employee.admissiondate,
            "mdmaddress": [
                {
                    "mdmaddress1": employee.address1,
                    "mdmaddress2": employee.address2,
                    "mdmaddress3": employee.address3,
                    "mdmcountry": employee.country,
                    "mdmstate": employee.state,
                    "mdmcity": employee.city,
                    "mdmzipcode": employee.zipcode,
                    "mdmaddresstype": employee.type,
                    "gmt": employee.gmt,
                }
            ],
        }

    return data
