from sqlalchemy.orm import Session
from api.department.department_repository import DepartmentRepository
from api.department.department_schema import DepartmentCreate, DepartmentResponse
from api.department.department_model import Department
from common.functions.get_object import get_object_or_404, get_list_or_404


def create_department(create_data: DepartmentCreate, db: Session ) -> DepartmentResponse:
    department_repository = DepartmentRepository(db)

    new_department = Department(
        id=create_data.id,
        name=create_data.name,
        states=create_data.status
    )

    created_income = department_repository.create_department(new_department)
    return created_income


def update_department_by_id(id: int, updateData: DepartmentCreate, db: Session) -> DepartmentResponse:
    department_repository = DepartmentRepository(db)

    department_to_update = department_repository.get_department_by_id(id)
    get_object_or_404(department_to_update)
   
    updated_department = department_repository.update_department(id, updateData)
    return updated_department


def delete_department_by_id(id: int, db: Session) -> DepartmentResponse:
    department_repository = DepartmentRepository(db)

    department_to_delete = department_repository.get_department_by_id(id)
    get_object_or_404(department_to_delete)

    deleted_department = department_repository.delete_department(id)
    return deleted_department


def get_department_by_id(id: int, db: Session ) -> DepartmentResponse:
    department_repository = DepartmentRepository(db)
    department = department_repository.get_all_department(id)
    
    return get_object_or_404(department)


def get_all_departments(db: Session ) -> list[DepartmentResponse]:
    department_repository = DepartmentRepository(db)
    all_departments = department_repository.get_all_department()

    return get_list_or_404(all_departments)