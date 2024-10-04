from flask import Blueprint

# Creamos un blueprint principal llamado "department_router"
department_router = Blueprint('department_router', __name__)

# Ruta raíz para verificar si el API está funcionando correctamente
@department_router.route("/", methods=["GET"])
def read_root():
    return {"message": "API's department_router"}