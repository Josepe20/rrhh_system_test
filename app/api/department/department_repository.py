from sqlalchemy.orm import Session
from sqlalchemy import extract
from api.department.department_model import Department


class DepartmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_department(self, department: Department) -> Department:
        self.db.add(department)
        self.db.commit()
        self.db.refresh(department)
        return department
    
    def update_department(self, department_id: int, new_data: dict) -> Department:
        department = self.db.query(Department).filter(Department.id == department_id).first()
        if department:
            for key, value in new_data.items():
                setattr(department, key, value)
            self.db.commit()
            self.db.refresh(department)
        return department

    def delete_department(self, department_id: int) -> Department:
        department = self.db.query(Department).filter(Department.id == department_id).first()
        if department:
            self.db.delete(department)
            self.db.commit()
        return department
    
    def get_department_by_id(self, department_id: int) -> Department:
        return self.db.query(Department).filter(Department.id == department_id).first()
    
    def get_all_department(self) -> list[Department]:
        return self.db.query(Department).all()