from flask import Blueprint

# Creamos un blueprint principal llamado "job_position_router"
job_position_router = Blueprint('job_position_router', __name__)

# Ruta raíz para verificar si el API está funcionando correctamente
@job_position_router.route("/", methods=["GET"])
def read_root():
    return {"message": "API's job_position_router"}