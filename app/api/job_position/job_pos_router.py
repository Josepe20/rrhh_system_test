from flask import Blueprint, request
from sqlalchemy.orm import Session
from dependencies import get_db_session
from common.functions.api_response import standard_response
from common.schemas.api_response_schema import StandardResponse
from api.job_position.job_pos_schema import JobPositionCreate, JobPositionResponse
from api.job_position import job_pos_view


# Creamos un blueprint principal llamado "job_position_router"
job_position_router = Blueprint('job_position_router', __name__)

# Ruta raíz para verificar si el API está funcionando correctamente
@job_position_router.route("/", methods=["GET"])
def read_root():
    return {"message": "API's job_position_router"}


@job_position_router.route("/create", methods=["POST"])
def create_job_position() -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    # Obtenemos los datos del request JSON
    create_data: JobPositionCreate = request.get_json()
    
    created_job_position = job_pos_view.create_job_position(create_data, db)
    return standard_response(201, 'job_position created successfully', created_job_position, JobPositionResponse)


@job_position_router.route("/update/<int:id>", methods=["PUT"])
def update_job_position_by_id(id: int) -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    # Obtenemos los datos del request JSON
    update_data: JobPositionCreate = request.get_json()

    updated_job_position = job_pos_view.update_job_position_by_id(id, update_data, db)
    return standard_response(200, 'job_position updated successfully', updated_job_position, JobPositionResponse)


@job_position_router.route("/delete/<int:id>", methods=["DELETE"])
def delete_job_position_by_id(id: int) -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    deleted_job_position = job_pos_view.delete_job_position_by_id(id, db)
    return standard_response(200, 'job_position deleted successfully', deleted_job_position, JobPositionResponse)


@job_position_router.route("/<int:id>", methods=["GET"])
def get_job_position_by_id(id: int) -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    job_position_found = job_pos_view.get_job_position_by_id(id, db)
    return standard_response(200, 'job_position found successfully', job_position_found, JobPositionResponse)


@job_position_router.route("/all", methods=["GET"])
def get_all_job_positions() -> StandardResponse:
    db: Session = get_db_session()  # Obtenemos la sesión correctamente
    job_positions_list = job_pos_view.get_all_job_positions(db)
    return standard_response(200, 'job_positions found successfully', job_positions_list, JobPositionResponse)
