from config.database import Base
from sqlalchemy import Column, Integer, String, Float, LargeBinary
from sqlalchemy.orm import relationship

class Busine(Base):
    
    __tablename__ = "Congregacion"

    idCongregacion = Column(Integer, primary_key = True)
    nombreCongregacion = Column(String)
    numeroCongregacion = Column(Integer)
    direccion = Column(String)