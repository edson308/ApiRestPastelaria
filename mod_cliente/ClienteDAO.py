from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import Depends
router = APIRouter()

import db 
from mod_cliente.ClienteModel import ClienteDB
import security

router = APIRouter(dependencies=[Depends(security.verify_token), Depends(security.verify_key)])


class Cliente(BaseModel):
    id: int = None
    nome: str
    matricula: str
    cpf: str
    telefone: str = None
    pega_fiado: int
    login: str = None
    senha: str = None
    
# Criar os endpoints de Cliente: GET, POST, PUT, DELETE
@router.get("/cliente/{id}", tags=["cliente"])
def get_cliente(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(ClienteDB).filter(ClienteDB.id == id).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()

@router.get("/cliente/", tags=["cliente"])   
def get_cliente():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(ClienteDB).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()

@router.post("/cliente/", tags=["cliente"])
def post_cliente(corpo: Cliente):
    try:
        session = db.Session()
        dados = ClienteDB(None, corpo.nome, corpo.matricula, corpo.cpf, corpo.telefone, corpo.pega_fiado, corpo.login, corpo.senha)

        session.add(dados)
        session.commit()
        return {"msg": "Cadastrado com sucesso!", "id": dados.id}, 200
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao cadastrar", "erro": str(e)}, 406
    finally:
        session.close()

@router.put("/cliente/{id}", tags=["cliente"])
def put_cliente(id: int, corpo: Cliente):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(
        ClienteDB.id == id).one()
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.matricula = corpo.matricula
        dados.pega_fiado = corpo.pega_fiado
        session.add(dados)
        session.commit()
        return {"msg": "Editado com sucesso!", "id": dados.id}, 201
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao editar", "erro": str(e)}, 406
    finally:
        session.close()

@router.delete("/cliente/{id}", tags=["cliente"])
def delete_cliente(id: int):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.id == id).one()
        session.delete(dados)
        session.commit()
        return {"msg": "Excluido com sucesso!", "id": dados.id}, 201
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao excluir", "erro": str(e)}, 406
    finally:
        session.close()