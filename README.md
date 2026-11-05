
# Proyecto SQLAlchemy 2.0

## Descripción

Este proyecto implementa un sistema de tracking para un proyecto de Data Science utilizando SQLAlchemy 2.0 y SQLite.

Permite definir y estructurar la información de los conjuntos de datos procesados y los experimentos de Machine Learning.

## Modelos definidos

### Dataset

Representa los conjuntos de datos utilizados en los proyectos.

- id: identificador único (clave primaria).
- name: nombre del dataset.
- source_url: dirección de origen.
- num_rows: cantidad de registros.

### ModelExperiment

Representa los experimentos de Machine Learning.

- id: identificador único (clave primaria).
- algorithm_name: nombre del algoritmo.
- accuracy: precisión del modelo.
- is_deployed: indica si el modelo está desplegado.

## Tecnologías utilizadas

- Python 3.13
- SQLAlchemy 2.0
- SQLite

## Estructura del proyecto

- models.py: define la clase Base y los modelos Dataset y ModelExperiment.
- main.py: crea la conexión, genera las tablas y realiza una prueba de los objetos.
- analytics.db: base de datos SQLite generada al ejecutar el programa.

## Cómo ejecutar el proyecto

1. Crear y activar un entorno virtual.
2. Instalar SQLAlchemy:

   pip install "sqlalchemy>=2.0,<2.1"

3. Ejecutar el programa:

   python main.py

## Resultado esperado

Al ejecutar main.py se genera el archivo analytics.db con las tablas datasets y model_experiments.

También se muestran por consola los objetos de prueba para verificar que el mapeo ORM funciona correctamente.
