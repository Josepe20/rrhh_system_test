from flask import Blueprint

# Creamos un blueprint principal llamado "employee_router"
employee_router = Blueprint('employee_router', __name__)

# Ruta raíz para verificar si el API está funcionando correctamente
@employee_router.route("/", methods=["GET"])
def read_root():
    return {"message": "API's employee_router"}