# Usa una imagen oficial de Python como base
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos e instálalos
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente al contenedor
COPY . .

# Expone el puerto que Render espera
EXPOSE 5000

# Comando para ejecutar la app con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]

