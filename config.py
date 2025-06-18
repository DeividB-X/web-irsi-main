import os

class Config:
    # Seguridad: clave secreta para sesiones Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave-secreta-en-desarrollo')

    # Conexión a la base de datos: PostgreSQL (en producción) o SQLite (en local)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///local.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración para envío de correos (opcional, si tu app lo usa)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
