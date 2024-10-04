from flask import Flask
# from flask_cors import CORS
from api.index_router import index_router  # Importar el blueprint principal

app = Flask(__name__)

# CORS server URIs (Angular Client App)
origins = [
    "http://localhost:8081",
    "http://127.0.0.1:8081",
    # Añadir otros orígenes si es necesario
]

# Configurar CORS
# CORS(app, resources={r"/*": {"origins": origins}})

# Register middlewares 


# Registrar el Blueprint principal
app.register_blueprint(index_router, url_prefix="/api")


# Ruta raíz para la aplicación
@app.route("/", methods=["GET"])
def read_root():
    return {"message": "Welcome to My RRHH System Web API"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

