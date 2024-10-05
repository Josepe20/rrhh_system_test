from marshmallow import Schema, fields

class JobPositionBase(Schema):
    name = fields.Str(required=True)
    status = fields.Bool(required=True)

class JobPositionCreate(JobPositionBase):
    pass 

class JobPositionResponse(JobPositionBase):
    id = fields.Int(dump_only=True)

class JobPositionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Bool(required=True)

    class Meta:
        model = "JobPosition"
