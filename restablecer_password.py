from app import create_app
from app.extensions import db
from app.models import Usuario

app = create_app()

with app.app_context():
    user = Usuario.query.filter_by(username="test@example.com").first()
    if user:
        user.set_password("password123")  # Nueva contraseña
        db.session.commit()
        print("✅ Contraseña restablecida correctamente.")
    else:
        print("❌ Usuario no encontrado.")