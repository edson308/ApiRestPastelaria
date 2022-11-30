from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import Depends
import db 
from mod_produto.ProdutoModel import ProdutoDB
import security

router = APIRouter(dependencies=[Depends(security.verify_token), Depends(security.verify_key)])

class Produto(BaseModel):
    id: int = None
    nome: str = None
    preco: float
    qtd: int
    descricao: str = None
    foto: bytes
    
# Criar os endpoints de Produto: GET, POST, PUT, DELETE
@router.get("/produto/{id}", tags=["produto"])
def get_produto(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(ProdutoDB).filter(ProdutoDB.id == id).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()
    
@router.get("/produto/", tags=["produto"])
def get_produto():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(ProdutoDB).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()

@router.post("/produto/", tags=["produto"])
def post_produto(corpo: Produto):
    try:
        session = db.Session()
        dados = ProdutoDB(None, corpo.nome, corpo.preco, corpo.qtd, corpo.foto, corpo.descricao)

        session.add(dados)
        session.commit()
        return {"msg": "Cadastrado com sucesso!", "id": dados.id}, 200
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao cadastrar", "erro": str(e)}, 406
    finally:
        session.close()
    

@router.put("/produto/{id}", tags=["produto"])
def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(
        ProdutoDB.id == id).one()
        dados.nome = corpo.nome
        dados.preco = corpo.preco
        dados.qtd = corpo.qtd
        dados.descricao = corpo.descricao
        dados.foto = corpo.foto
        session.add(dados)
        session.commit()
        return {"msg": "Editado com sucesso!", "id": dados.id}, 201
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao editar", "erro": str(e)}, 406
    finally:
        session.close()

@router.delete("/produto/{id}", tags=["produto"])
def delete_produto(id: int):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(ProdutoDB.id == id).one()
        session.delete(dados)
        session.commit()
        return {"msg": "Excluido com sucesso!", "id": dados.id}, 201
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao excluir", "erro": str(e)}, 406
    finally:
        session.close()