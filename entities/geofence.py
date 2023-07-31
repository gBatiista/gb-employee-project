from pydantic import BaseModel


class Geofence(BaseModel):
    address1: str
    address2: str
    address3: str
    country: str
    state: str
    city: str
    gmt: str
    zipcode: str
    type: str
    employeecode: str
    taxid: str
