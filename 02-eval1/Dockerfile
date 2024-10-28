# imagen base de python
FROM python:3.9-alpine

# directorio de trabajo
WORKDIR /app

# copia los archivos 
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# pubicams puerto 8888
EXPOSE 8888

# ejecuta la la aplicación
ENTRYPOINT ["python", "app.py"]

