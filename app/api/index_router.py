from flask import Blueprint
from api.department.department_router import department_router
from api.employees.employee_router import employee_router
from api.job_position.job_pos_router import job_position_router

# Creamos un blueprint principal llamado "index_router"
index_router = Blueprint('index_router', __name__)

# Registrar el Blueprint de modulos
index_router.register_blueprint(department_router, url_prefix="/department")
index_router.register_blueprint(employee_router, url_prefix="/employee")
index_router.register_blueprint(job_position_router, url_prefix="/job_position")

# Ruta raíz para verificar si el API está funcionando correctamente
@index_router.route("/", methods=["GET"])
def read_root():
    return {"message": "API's index_router"}
