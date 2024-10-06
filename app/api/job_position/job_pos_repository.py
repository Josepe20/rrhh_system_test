from sqlalchemy.orm import Session
from sqlalchemy import extract
from api.job_position.job_pos_model import JobPosition


class JobPositionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_job_position(self, job_position: JobPosition) -> JobPosition:
        self.db.add(job_position)
        self.db.commit()
        self.db.refresh(job_position)
        return job_position
    
    def update_job_position(self, job_position_id: int, new_data: dict) -> JobPosition:
        job_position = self.db.query(JobPosition).filter(JobPosition.id == job_position_id).first()
        if job_position:
            for key, value in new_data.items():
                setattr(job_position, key, value)
            self.db.commit()
            self.db.refresh(job_position)
        return job_position

    def delete_job_position(self, job_position_id: int) -> JobPosition:
        job_position = self.db.query(JobPosition).filter(JobPosition.id == job_position_id).first()
        if job_position:
            self.db.delete(job_position)
            self.db.commit()
        return job_position
    
    def get_job_position_by_id(self, job_position_id: int) -> JobPosition:
        return self.db.query(JobPosition).filter(JobPosition.id == job_position_id).first()
    
    def get_all_job_positions(self) -> list[JobPosition]:
        return self.db.query(JobPosition).all()