# Usa una imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala dependencias del sistema necesarias para psycopg2 y pyodbc
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    libpq-dev \
    unixodbc-dev \
    && pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará Flask (Render usa por defecto el 10000, pero 0.0.0.0:PORT es lo importante)
EXPOSE 10000

# Comando para ejecutar la app
CMD ["python", "run.py"]
