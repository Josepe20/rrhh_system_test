from flask import Blueprint, request
from sqlalchemy.orm import Session
from dependencies import get_db_session
from common.functions.api_response import standard_response
from common.schemas.api_response_schema import StandardResponse
from api.employees.employee_schema import EmployeeCreate, EmployeeResponse
from api.employees import employee_view


# Creamos un blueprint principal llamado "employee_router"
employee_router = Blueprint('employee_router', __name__)

# Ruta raíz para verificar si el API está funcionando correctamente
@employee_router.route("/", methods=["GET"])
def read_root():
    return {"message": "API's employee_router"}


@employee_router.route("/create", methods=["POST"])
def create_employee() -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    # Obtenemos los datos del request JSON
    create_data: EmployeeCreate = request.get_json()

    created_employee = employee_view.create_employee(create_data, db)
    return standard_response(201, 'employee created successfully', created_employee, EmployeeResponse)


@employee_router.route("/update/<int:id>", methods=["PUT"])
def update_employee(id: int) -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    # Obtenemos los datos del request JSON
    update_data: EmployeeCreate = request.get_json()

    updated_employee = employee_view.update_employee_by_id(id, update_data, db)
    return standard_response(200, 'employee updated successfully', updated_employee, EmployeeResponse)


@employee_router.route("/delete/<int:id>", methods=["DELETE"])
def delete_employee(id: int) -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    deleted_employee = employee_view.delete_employee_by_id(id, db)
    return standard_response(200, 'employee deleted successfully', deleted_employee, EmployeeResponse)


@employee_router.route("/<int:id>", methods=["GET"])
def get_employee_by_id(id: int) -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    employee = employee_view.get_employee_by_id(id, db)
    return standard_response(200, 'employee found successfully', employee, EmployeeResponse)


@employee_router.route("/all", methods=["GET"])
def get_all_employees() -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    employee_list = employee_view.get_all_job_employees(db)
    return standard_response(200, 'employees found successfully', employee_list, EmployeeResponse)