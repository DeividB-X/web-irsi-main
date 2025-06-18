from app.extensions import db
from app import create_app

def ejecutar_sql():
    app = create_app()
    with app.app_context():
        # Lee y ejecuta el archivo SQL
        with open('MSSQL/init_postgres.sql', 'r', encoding='utf-8') as f:
            sql_script = f.read()
            for statement in sql_script.strip().split(';'):
                if statement.strip():
                    db.session.execute(statement)
            db.session.commit()
        print("Script SQL ejecutado correctamente")

if __name__ == "__main__":
    ejecutar_sql()