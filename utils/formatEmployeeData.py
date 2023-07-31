from entities.employee import Employee


def formatEmployeeData(employee: Employee | list[Employee]):
    data = None

    employeeKeys = [
        "isterminated",
        "admissiondate",
        "personid",
        "taxid",
        "employeecode",
        "email",
        "name",
    ]

    if type(employee) == list:
        data = [
            {key: value for key, value in item if key in employeeKeys}
            for item in employee
        ]

    else:
        data = {key: value for key, value in employee if key in employeeKeys}

    return data
