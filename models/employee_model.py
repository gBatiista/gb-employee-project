from pycarol import Carol, ApiKeyAuth, Staging, Query, BQ
from pycarol.filter import TYPE_FILTER, TERM_FILTER, Filter
import os
from dotenv import load_dotenv

load_dotenv()

carol = Carol(
    domain=os.getenv("DOMAIN"),
    app_name=os.getenv("APP_NAME"),
    auth=ApiKeyAuth(api_key=os.getenv("X_AUTH_KEY")),
    connector_id=os.getenv("CONNECTOR"),
    organization=os.getenv("ORGANIZATION"),
)

bq = BQ(carol)

staging = Staging(carol)


async def getAllEmployees():
    json_query = (
        Filter.Builder()
        .must(TYPE_FILTER(value="gbemployeeprojectGolden"))
        .build()
        .to_json()
    )

    query = (
        Query(carol, page_size=50, print_status=True, only_hits=True, max_hits=5000)
        .query(json_query)
        .go()
    )
    return query.results


async def getByEmployeeCodeAndTaxId(taxId, employeeCode):
    json_query = (
        Filter.Builder()
        .must(TYPE_FILTER(value="gbemployeeprojectGolden"))
        .must(TERM_FILTER(key="mdmGoldenFieldAndValues.mdmtaxid.raw", value=taxId))
        .must(
            TERM_FILTER(
                key="mdmGoldenFieldAndValues.employeecode.raw", value=employeeCode
            )
        )
        .build()
        .to_json()
    )

    query = (
        Query(carol, page_size=50, print_status=True, only_hits=True, max_hits=5000)
        .query(json_query)
        .go()
    )
    return query.results


async def getAllByTaxId(taxId):
    json_query = (
        Filter.Builder()
        .must(TYPE_FILTER(value="gbemployeeprojectGolden"))
        .must(TERM_FILTER(key="mdmGoldenFieldAndValues.mdmtaxid.raw", value=taxId))
        .build()
        .to_json()
    )

    query = (
        Query(carol, page_size=50, print_status=True, only_hits=True, max_hits=5000)
        .query(json_query)
        .go()
    )
    return query.results


async def createEmployee(dataToEmployeeStg, dataToGeofenceStg, dataToRT):
    staging.send_data(
        staging_name="employee",
        data=dataToEmployeeStg,
        step_size=50,
        connector_id=os.getenv("CONNECTOR"),
        print_stats=True,
    )

    staging.send_data(
        staging_name="geofence",
        data=dataToGeofenceStg,
        step_size=50,
        connector_id=os.getenv("CONNECTOR"),
        print_stats=True,
    )

    # Criação do preview no RT

    url = os.getenv("PREVIEW_URL")

    response = carol.call_api(path=url, method="POST", data=dataToRT)

    return response


async def addGeofence(dataToGeofenceStaging):
    staging.send_data(
        staging_name="geofence",
        data=dataToGeofenceStaging,
        step_size=50,
        connector_id=os.getenv("CONNECTOR"),
        print_stats=True,
    )


async def updateEmployee(dataToUpdate, dataToRT):
    staging.send_data(
        staging_name="employee",
        data=dataToUpdate,
        step_size=50,
        connector_id=os.getenv("CONNECTOR"),
        print_stats=True,
    )

    # Criação do preview no RT

    url = os.getenv("PREVIEW_URL")

    response = carol.call_api(path=url, method="POST", data=dataToRT)

    return response


async def deleteEmployee(taxId: str, employeeCode: str, id: str):
    # Delete Geofence Staging

    query_str = (
        "SELECT * FROM stg_gbemployeeproject_geofence WHERE taxid = '"
        + taxId
        + "' AND employeecode = '"
        + employeeCode
        + "'"
    )
    result = bq.query(query_str)

    result_dict = result.to_dict()

    if len(result_dict.values()) == 0:
        return False

    codes = list(result_dict["code"].values())

    for code in codes:
        staging.send_data(
            staging_name="geofence",
            data={"code": code, "mdmDeleted": True},
            step_size=50,
            connector_id=os.getenv("CONNECTOR"),
            print_stats=True,
        )

    # Delete Employee Staging

    staging.send_data(
        staging_name="employee",
        data={
            "taxid": taxId,
            "employeecode": employeeCode,
            "mdmDeleted": True,
        },
        step_size=50,
        connector_id=os.getenv("CONNECTOR"),
        print_stats=True,
    )

    # Delete RT

    url = os.getenv("DELETE_URL") + id + "?propagateSourceDeletion=true"
    print(url)

    try:
        return carol.call_api(path=url, method="DELETE")
    except Exception:
        return False
