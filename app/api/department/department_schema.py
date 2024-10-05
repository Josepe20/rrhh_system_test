from marshmallow import Schema, fields

class DepartmentBase(Schema):
    name = fields.Str(required=True)
    status = fields.Bool(required=True)

class DepartmentCreate(DepartmentBase):
    pass 

class DepartmentResponse(DepartmentBase):
    id = fields.Int(dump_only=True)

class DepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Bool(required=True)

    class Meta:
        # Especifica que este schema es compatible con modelos de SQLAlchemy
        model = "Department"
