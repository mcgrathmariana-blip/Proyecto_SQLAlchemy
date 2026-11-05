
from sqlalchemy import String, Integer, Float, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Clase base para todos nuestros modelos
class Base(DeclarativeBase):
    pass


# Modelo que representa los datasets
class Dataset(Base):
    __tablename__ = "datasets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    source_url: Mapped[str] = mapped_column(String(255), nullable=False)
    num_rows: Mapped[int] = mapped_column(Integer, nullable=False)


# Modelo que representa los experimentos de Machine Learning
class ModelExperiment(Base):
    __tablename__ = "model_experiments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    algorithm_name: Mapped[str] = mapped_column(String(100), nullable=False)
    accuracy: Mapped[float] = mapped_column(Float, nullable=False)
    is_deployed: Mapped[bool] = mapped_column(Boolean, default=False)
