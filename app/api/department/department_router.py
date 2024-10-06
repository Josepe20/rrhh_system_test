from flask import Blueprint, request
from sqlalchemy.orm import Session
from dependencies import get_db_session
from common.functions.api_response import standard_response
from common.schemas.api_response_schema import StandardResponse
from api.department.department_schema import DepartmentCreate, DepartmentResponse
from api.department import department_view

# Creamos un blueprint principal llamado "department_router"
department_router = Blueprint('department_router', __name__)

# Ruta raíz para verificar si el API está funcionando correctamente
@department_router.route("/", methods=["GET"])
def read_root():
    return {"message": "API's department_router"}


@department_router.route("/create", methods=["POST"])
def create_department() -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    # Obtenemos los datos del request JSON
    create_data: DepartmentCreate = request.get_json()

    created_department = department_view.create_department(create_data, db)
    return standard_response(201, 'department created successfully', created_department, DepartmentResponse)


@department_router.route("/update/<int:id>", methods=["PUT"])
def update_department_by_id(id: int) -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    # Obtenemos los datos del request JSON
    update_data: DepartmentCreate = request.get_json()

    updated_department = department_view.update_department_by_id(id, update_data, db)
    return standard_response(200, 'department updated successfully', updated_department, DepartmentResponse)


@department_router.route("/delete/<int:id>", methods=["DELETE"])
def delete_department_by_id(id: int) -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    deleted_department = department_view.delete_department_by_id(id, db)
    return standard_response(200, 'department deleted successfully', deleted_department, DepartmentResponse)


@department_router.route("/<int:id>", methods=["GET"])
def get_department_by_id(id: int) -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    department_found = department_view.get_department_by_id(id, db)
    return standard_response(200, 'department found successfully', department_found, DepartmentResponse)


@department_router.route("/all", methods=["GET"])
def get_all_departments() -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    department_list = department_view.get_all_departments(db)
    return standard_response(200, 'departments found successfully', department_list, DepartmentResponse)
