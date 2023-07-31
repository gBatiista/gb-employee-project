from pycarol import Carol, ApiKeyAuth, Staging
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

staging = Staging(carol)


async def createEmployee(dataToEmployeeStaging, dataToGeofenceStaging):
    staging.send_data(
        staging_name="employee",
        data=dataToEmployeeStaging,
        step_size=50,
        connector_id=os.getenv("CONNECTOR"),
        print_stats=True,
    )

    staging.send_data(
        staging_name="geofence",
        data=dataToGeofenceStaging,
        step_size=50,
        connector_id=os.getenv("CONNECTOR"),
        print_stats=True,
    )

    # falta criar o preview no RT


async def addGeofence(dataToGeofenceStaging):
    staging.send_data(
        staging_name="geofence",
        data=dataToGeofenceStaging,
        step_size=50,
        connector_id=os.getenv("CONNECTOR"),
        print_stats=True,
    )

    # falta criar o preview no RT
