import uuid
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UsuarioModel(Base):
    __tablename__ = "usuarios"
    
    usuario_id = Column('usuario_id', Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    usuario_cpf = Column(String, unique=True, index=True)
    usuario_nome = Column(String)
    usuario_email = Column(String, unique=True, index=True)
    usuario_senha = Column(String)
    usuario_telefone = Column(String)
    enderecos = relationship("EnderecoModel", back_populates="usuario")