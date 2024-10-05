from database import SessionLocal

# Función para obtener la sesión de la base de datos
def get_db_session():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
