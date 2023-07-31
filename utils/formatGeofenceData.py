from entities.employee import Employee
import hashlib


def formatGeofenceData(employee: Employee | list[Employee]):
    data = None
    geofenceKeys = [
        "address1",
        "address2",
        "address3",
        "country",
        "state",
        "city",
        "gmt",
        "employeecode",
        "taxid",
        "zipcode",
        "type",
    ]

    if type(employee) == list:
        data = [
            {key: value for key, value in item if key in geofenceKeys}
            for item in employee
        ]

        for item in data:
            item["code"] = hashlib.sha256(
                (
                    item["address1"]
                    + item["address2"]
                    + item["address3"]
                    + item["country"]
                    + item["state"]
                    + item["city"]
                    + item["gmt"]
                    + item["employeecode"]
                    + item["taxid"]
                    + item["zipcode"]
                    + item["type"]
                ).encode()
            ).hexdigest()

    else:
        data = {
            **{key: value for key, value in employee if key in geofenceKeys},
            "code": hashlib.sha256(
                (
                    employee.address1
                    + employee.address2
                    + employee.address3
                    + employee.country
                    + employee.state
                    + employee.city
                    + employee.gmt
                    + employee.employeecode
                    + employee.taxid
                    + employee.zipcode
                    + employee.type
                ).encode()
            ).hexdigest(),
        }

    return data
