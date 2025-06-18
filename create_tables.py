from app import create_app
from app.extensions import db
from app.models import Usuario, Estudiante

def create_all_tables():
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Tablas creadas (Usuarios y Estudiantes)")

if __name__ == "__main__":
    create_all_tables()