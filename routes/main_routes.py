from fastapi import APIRouter

from controllers import employee_controller as employee

router = APIRouter()

router.include_router(employee.router, prefix="/employee")
