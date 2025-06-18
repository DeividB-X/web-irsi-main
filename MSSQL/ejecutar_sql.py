#!/usr/bin/env python3
import sys
import os

# ————— Ajuste de la ruta para poder importar 'app' —————
# Dir actual: .../web-irsi-main/MSSQL/ejecutar_sql.py
# Queremos añadir .../web-irsi-main al path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
# ————————————————————————————————————————————————

from sqlalchemy import text
from app.extensions import db
from app import create_app

def ejecutar_sql():
    app = create_app()
    with app.app_context():
        # 1) Crear tablas e índices
        sql_path = os.path.join(os.path.dirname(__file__), "init_postgres.sql")
        with open(sql_path, "r", encoding="utf-8") as f:
            sql_content = f.read()

        # Ejecutamos cada bloque separado por ';'
        statements = [stmt.strip() for stmt in sql_content.split(";") if stmt.strip()]
        for stmt in statements:
            db.session.execute(text(stmt))

        # 2) Insertar usuarios de prueba, ignorando duplicados
        insert_usuarios = """
        INSERT INTO Usuarios (username, password_hash, role) VALUES
        ('test@example.com', '$2b$12$hqmlMHETNGRGX3tqFaHrz.81nRIG2VqvXBwo6V6.3dfSJs2/7XVIK', 'admin'),
        ('consulta_user@example.com', '$2b$12$wF9XKqbN7WG2QCrarYxPzOwufTNC1C092X/NZMChYOK3mtPK/K3Jm', 'consulta'),
        ('director_user@example.com', '$2b$12$WHLBk6WjOu83JYPWJkZymuXbLub71K8S6s0gdrSGLFbhWdbgaPquO', 'director'),
        ('consultor@gmail.com', '$2b$12$YQ5Mq648tYdJpwmUQYXFFe8sztPQdxwNcsGLIRyHQ1uQ5WcFETHMG', 'consulta')
        ON CONFLICT (username) DO NOTHING;
        """
        db.session.execute(text(insert_usuarios))

        db.session.commit()
        print("✅ Tablas e índices creados, y usuarios insertados sin duplicados.")


if __name__ == "__main__":
    ejecutar_sql()