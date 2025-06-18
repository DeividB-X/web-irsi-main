-- init_postgres.sql

-- Crear tabla Usuarios si no existe
CREATE TABLE IF NOT EXISTS Usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL CHECK (role IN ('admin', 'director', 'consulta')),
    two_factor_code VARCHAR(6),
    two_factor_expiry TIMESTAMP
);

-- Crear tabla Estudiantes si no existe
CREATE TABLE IF NOT EXISTS Estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    senas_direccion VARCHAR(500),
    grado_academico VARCHAR(100) NOT NULL,
    dni VARCHAR(20) UNIQUE NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    correo VARCHAR(255) NOT NULL,
    telefono VARCHAR(20),
    anio_solicitud INT NOT NULL
);

-- Crear índices si no existen
CREATE INDEX IF NOT EXISTS idx_dni ON Estudiantes(dni);
CREATE INDEX IF NOT EXISTS idx_username ON Usuarios(username);