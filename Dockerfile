# Usar la imagen oficial de Python 3.10 como base
FROM python:3.10

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido de la carpeta actual al directorio de trabajo en la imagen
COPY . .

# Ejecutar la aplicación cuando se inicie el contenedor
CMD ["gunicorn", "main:app"]
