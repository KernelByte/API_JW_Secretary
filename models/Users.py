from config.database import Base
from sqlalchemy import Column, Integer, String, LargeBinary,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    
    __tablename__ = "Users"

    idUser = Column(Integer, primary_key = True, index=True)
    nameUser = Column(String)
    mailUser = Column(String)
    passwordUser = Column(String)
    idRoleUser = Column(Integer,ForeignKey("Roles.idRole"),nullable=True)
    tokenUser = Column(String,nullable=True)
    #profilePicture = Column(LargeBinary)
    idCongregationUser = Column(Integer)
        #Integer,ForeignKey("Congregacion.idCongregacion"),nullable=True)