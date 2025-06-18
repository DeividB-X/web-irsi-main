from app import create_app
from app.extensions import db
from app.models import Usuario

def insert_users():
    app = create_app()
    with app.app_context():
        # Crear usuarios de ejemplo
        admin = Usuario(username="admin@example.com", role="admin")
        admin.set_password("adminpassword")

        director = Usuario(username="director@example.com", role="director")
        director.set_password("directorpassword")

        consulta = Usuario(username="consulta@example.com", role="consulta")
        consulta.set_password("consultapassword")

        # Solo agregar si no existen
        for user in (admin, director, consulta):
            if not Usuario.query.filter_by(username=user.username).first():
                db.session.add(user)

        db.session.commit()
        print("✅ Usuarios insertados con éxito")

if __name__ == "__main__":
    insert_users()