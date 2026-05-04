# API de Ventas con Flask

API desarrollada en Python con Flask para procesar y exponer datos de ventas.

## Funcionalidades

- Procesamiento de datos desde CSV
- Cálculo de ventas totales
- Ranking de productos
- Endpoints dinámicos
- Manejo de errores

## Endpoints

- /ventas → devuelve todas las ventas agrupadas
- /ventas/<producto> → filtra por producto
- /top → ranking completo
- /top/<n> → top N productos

## Tecnologías

- Python
- Flask
- Pandas

## Cómo ejecutar

bash pip install -r requirements.txt python app.py

## Ejemplo

http://127.0.0.1:5000/top/3

## Objetivo

Demostrar habilidades en desarrollo backend, manejo de datos y construcción de APIs