
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from controllers.usuario import create_usuario, delete_usuario, put_usuario, read_usuario
from schemas.usuario import UsuarioPartial, Usuario

from middlewares.isContentTypeApplicationJson import IsContentTypeApplicationJson
from starlette.middleware.base import BaseHTTPMiddleware

# Cria uma instância do FastAPI
app = FastAPI()

# URL de conexão com o banco de dados SQLite
DATABASE_URL = "sqlite:///./teste.db"

# Cria uma conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe base declarativa para definir modelos do SQLAlchemy
Base = declarative_base()

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

is_content_type_application_json = IsContentTypeApplicationJson()
app.add_middleware(BaseHTTPMiddleware, dispatch=is_content_type_application_json)

# Define a rota POST para criar um usuário
@app.post("/usuario/", response_model=UsuarioPartial)
def criar_usuario(usuario: UsuarioPartial):
    return create_usuario(usuario, SessionLocal)
    
# Define a rota GET para ler informações de um usuário pelo ID
@app.get("/usuario/{usuario_id}", response_model=Usuario)
def ler_usuario(usuario_id: int):
    return read_usuario(usuario_id, SessionLocal)

@app.put("/usuario/{usuario_id}", response_model=Usuario)
def atualizar_usuario(usuario_id: int, usuario: UsuarioPartial):
    return put_usuario(usuario_id, usuario, SessionLocal)

@app.delete("/usuario/{usuario_id}", response_model=Usuario)
def deletar_usuario(usuario_id: int):
    return delete_usuario(usuario_id, SessionLocal)