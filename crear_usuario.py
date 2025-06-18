from app import create_app
from app.extensions import db
from app.models import Usuario

def crear_usuario():
    app = create_app()
    with app.app_context():
        username = "test@example2.com"
        password = "$2b$12$hqmlMHETNGRGX3tqFaHrz.81nRIG2VqvXBwo6V6.3dfSJs2/7XVIK"
        role = "admin"

        # Verificar si ya existe
        usuario = Usuario.query.filter_by(username=username).first()
        if usuario:
            print(f"✅ El usuario '{username}' ya existe.")
        else:
            nuevo_usuario = Usuario(username=username, role=role)
            nuevo_usuario.set_password(password)  # Asegúrate que tu modelo tenga esta función
            db.session.add(nuevo_usuario)
            db.session.commit()
            print(f"✅ Usuario '{username}' creado correctamente con rol '{role}'.")

if __name__ == "__main__":
    crear_usuario()