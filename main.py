
from sqlalchemy import create_engine
from models import Base, Dataset, ModelExperiment


# Crear la conexion con la base de datos SQLite
engine = create_engine("sqlite:///analytics.db", echo=True)


# Crear las tablas definidas en models.py
Base.metadata.create_all(engine)


# Crear un objeto Dataset de ejemplo
dataset = Dataset(
    name="Telecom Churn",
    source_url="https://example.com/telecom-churn.csv",
    num_rows=7043
)


# Crear un objeto ModelExperiment de ejemplo
experimento = ModelExperiment(
    algorithm_name="Random Forest",
    accuracy=0.85,
    is_deployed=True
)


# Mostrar los objetos por consola
print("\n--- PRUEBA DEL MAPEO ORM ---")

print("Dataset:")
print("Nombre:", dataset.name)
print("Origen:", dataset.source_url)
print("Cantidad de registros:", dataset.num_rows)

print("\nExperimento:")
print("Algoritmo:", experimento.algorithm_name)
print("Accuracy:", experimento.accuracy)
print("Desplegado:", experimento.is_deployed)

print("\n¡Mapeo ORM funcionando correctamente!")
