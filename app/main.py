from flask import Flask
from database import SessionLocal
from sqlalchemy import text
from flask_cors import CORS
from api.index_router import index_router  # Importar el blueprint principal
from middlewares.exception_middleware import ExceptionHandlingMiddleware

app = Flask(__name__)

# CORS server URIs (Angular Client App)
origins = [
    "http://localhost:8081",
    "http://127.0.0.1:8081",
    # Añadir otros orígenes si es necesario
]

# Configurar CORS
CORS(app, resources={r"/*": {"origins": origins}})

# Register middlewares 
ExceptionHandlingMiddleware(app)

# Registrar el Blueprint principal
app.register_blueprint(index_router, url_prefix="/api")


# Ruta raíz para la aplicación
@app.route("/", methods=["GET"])
def read_root():
    return {"message": "Welcome to My RRHH System Web API"}


@app.route('/check_db')
def check_db():
    try:
        db = SessionLocal()
        result = db.execute(text('SELECT 1')).scalar()  # Usar text() para consultas sin procesar
        return f"DB connection successful! Result: {result}", 200
    except Exception as e:
        return f"DB connection failed: {e}", 500
    finally:
        db.close()



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

