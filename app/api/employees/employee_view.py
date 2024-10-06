from sqlalchemy.orm import Session
from api.employees.employee_repository import EmployeeRepository
from api.employees.employee_schema import EmployeeCreate, EmployeeResponse
from api.employees.employee_model import Employee
from common.functions.get_object import get_object_or_404, get_list_or_404


def create_employee(create_data: EmployeeCreate, db: Session ) -> EmployeeResponse:
    employee_repository = EmployeeRepository(db)

    new_job_employee = Employee(
        first_name = create_data.first_name,
        last_name = create_data.last_name,
        address = create_data.address,
        birth_date = create_data.birth_date,
        department_id = create_data.department_id,
        job_position_id = create_data.job_position_id,
    )

    created_employee = employee_repository.create_employee(new_job_employee)
    return created_employee


def update_employee_by_id(id: int, updateData: EmployeeCreate, db: Session) -> EmployeeResponse:
    employee_repository = EmployeeRepository(db)

    employee_to_update = employee_repository.get_employee_by_id(id)
    get_object_or_404(employee_to_update)
   
    updated_employee = employee_repository.update_employee(id, updateData)
    return updated_employee


def delete_employee_by_id(id: int, db: Session) -> EmployeeResponse:
    employee_repository = EmployeeRepository(db)

    employee_to_delete = employee_repository.get_employee_by_id(id)
    get_object_or_404(employee_to_delete)

    deleted_employee = employee_repository.delete_employee(id)
    return deleted_employee


def get_employee_by_id(id: int, db: Session ) -> EmployeeResponse:
    employee_repository = EmployeeRepository(db)
    employee = employee_repository.get_employee_by_id(id)
    
    return get_object_or_404(employee)


def get_all_job_employees(db: Session ) -> list[EmployeeResponse]:
    employee_repository = EmployeeRepository(db)
    employees = employee_repository.get_all_employees()

    return get_list_or_404(employees)