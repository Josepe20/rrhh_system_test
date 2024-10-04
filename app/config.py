from decouple import config
from marshmallow import Schema, fields, post_load

# Clase de configuración usando Marshmallow
class AppConfigSchema(Schema):
    app_name = fields.Str(required=True)
    admin_email = fields.Email(required=True)
    items_per_user = fields.Int(missing=50)

    @post_load
    def make_config(self, data, **kwargs):
        return AppConfig(**data)

# Clase para almacenar la configuración
class AppConfig:
    def __init__(self, app_name, admin_email, items_per_user):
        self.app_name = app_name
        self.admin_email = admin_email
        self.items_per_user = items_per_user

# Cargar la configuración desde variables de entorno usando python-decouple
config_data = {
    "app_name": config("APP_NAME", default="RRHH_SYSTEM"),
    "admin_email": config("ADMIN_EMAIL"),
    "items_per_user": config("ITEMS_PER_USER", cast=int, default=50)
}

# Instancia de configuración validada
schema = AppConfigSchema()
settings = schema.load(config_data)
