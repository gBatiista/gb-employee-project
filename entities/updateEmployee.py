from pydantic import BaseModel


class UpdateEmployee(BaseModel):
    isterminated: bool
    admissiondate: str
    personid: str
    email: str
    name: str
    taxid: str
    employeecode: str
