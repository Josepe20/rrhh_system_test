from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from api.department.department_schema import DepartmentSchema
from api.job_position.job_pos_schema import JobPositionSchema

class EmployeeBase(Schema):
    department_id = fields.Int(required=True)
    job_position_id = fields.Int(required=True)

class EmployeeCreate(EmployeeBase):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    address = fields.Str(required=True)
    birth_date = fields.Date(required=True)

class EmployeeResponse(EmployeeBase):
    id = fields.Int(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    address = fields.Str()
    birth_date = fields.Date()
    department = fields.Nested(DepartmentSchema, dump_only=True)
    job_position = fields.Nested(JobPositionSchema, dump_only=True)

    class Meta:
        model = "Employee"
        # Indicar a Marshmallow que use los modelos SQLAlchemy para la serialización
        sqla_session = True
