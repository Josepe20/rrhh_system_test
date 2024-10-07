from sqlalchemy.orm import Session
from api.job_position.job_pos_repository import JobPositionRepository
from api.job_position.job_pos_schema import JobPositionCreate, JobPositionResponse
from api.job_position.job_pos_model import JobPosition
from common.functions.get_object import get_object_or_404, get_list_or_404


def create_job_position(create_data: JobPositionCreate, db: Session ) -> JobPositionResponse:
    job_position_repository = JobPositionRepository(db)

    new_job_position = JobPosition(
        name=create_data["name"],
        states=create_data["status"]
    )

    created_job_position = job_position_repository.create_job_position(new_job_position)
    return created_job_position


def update_job_position_by_id(id: int, updateData: JobPositionCreate, db: Session) -> JobPositionResponse:
    job_position_repository = JobPositionRepository(db)

    job_position_to_update = job_position_repository.get_job_position_by_id(id)
    get_object_or_404(job_position_to_update)
   
    updated_job_position = job_position_repository.update_job_position(id, updateData)
    return updated_job_position


def delete_job_position_by_id(id: int, db: Session) -> JobPositionResponse:
    job_position_repository = JobPositionRepository(db)

    job_position_to_delete = job_position_repository.get_job_position_by_id(id)
    get_object_or_404(job_position_to_delete)

    deleted_job_position = job_position_repository.delete_job_position(id)
    return deleted_job_position


def get_job_position_by_id(id: int, db: Session ) -> JobPositionResponse:
    job_position_repository = JobPositionRepository(db)
    job_position = job_position_repository.get_job_position_by_id(id)
    
    return get_object_or_404(job_position)


def get_all_job_positions(db: Session ) -> list[JobPositionResponse]:
    job_position_repository = JobPositionRepository(db)
    all_job_positions = job_position_repository.get_all_job_positions()

    return get_list_or_404(all_job_positions)