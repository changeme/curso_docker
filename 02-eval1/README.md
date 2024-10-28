# Proyecto Flask en Docker

## Descripción
Este proyecto utiliza Flask para crear un servidor web que responde a solicitudes HTTP. 

Elegí Flask porque es un framework ligero y estoy intentando aprender este lenguaje de programación.

Aun así, no he llegado a la parte de interfaz web, ni tampoco soy muy avezado en progración, no me gusta mucho ni soy del rubro, asi que chatgpt al rescate para programar

## Instrucciones de Uso

1. Clona el repositorio o copia los archivos a tu máquina local.
2. Abre una terminal y navega hasta la carpeta del proyecto.
3. Construye la imagen de Docker:

   ```bash
   docker build -t diego_sanchez_entrega1 .
   ```

4. Ejecuta el contenedor

## Resultados esperados

GET a http://localhost:8080/mi_endpoint?ABC=123
Output Esperado: {"result": "XYZ"}

GET a http://localhost:8080/mi_endpoint?ABC=456
Output Esperado: {"result": "Invalid input"}

   ```bash
   docker run -p 8888:8888 -rm diego_sanchez_entrega1
   ```

5. Acceder vía navegador a `http://localhost:8888/endpoint?ABC=132`
6. Eliminar la imagen con `docker rmi diego_sanchez_entrega1`
