from marshmallow import Schema, fields

# generics interface
class StandardResponse(Schema):
    status = fields.Int(required=True)
    message = fields.Str(required=True)
    data = fields.Raw(required=False)  # `fields.Raw` acepta cualquier tipo de dato
