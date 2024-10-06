from sqlalchemy.orm import Session
from sqlalchemy import extract
from api.job_position.job_pos_model import JobPosition
from api.employees.employee_model import Employee


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, employee: Employee) -> Employee:
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return employee
    
    def update_employee(self, employee_id: int, new_data: dict) -> Employee:
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            for key, value in new_data.items():
                setattr(employee, key, value)
            self.db.commit()
            self.db.refresh(employee)
        return employee

    def delete_employee(self, employee_id: int) -> Employee:
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            self.db.delete(employee)
            self.db.commit()
        return employee
    
    def get_employee_by_id(self, employee_id: int) -> Employee:
        return self.db.query(Employee).filter(Employee.id == employee_id).first()
    
    def get_all_employees(self) -> list[Employee]:
        return self.db.query(Employee).all()