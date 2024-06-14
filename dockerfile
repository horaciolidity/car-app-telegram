# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia los archivos necesarios
COPY requirements.txt ./
COPY bot.py ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar el bot
CMD ["python", "./bot.py"]
