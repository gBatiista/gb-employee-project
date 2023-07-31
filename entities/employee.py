from pydantic import BaseModel


class Employee(BaseModel):
    isterminated: bool
    admissiondate: str
    personid: str
    taxid: str
    employeecode: str
    email: str
    name: str
    address1: str
    address2: str
    address3: str
    country: str
    state: str
    city: str
    gmt: str
    zipcode: str
    type: str
