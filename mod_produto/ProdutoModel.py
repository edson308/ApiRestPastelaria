import db
from sqlalchemy import Column, VARCHAR, Integer, FLOAT, BLOB
# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    preco = Column(FLOAT(precision=10, decimal_return_scale=None), nullable=False)
    qtd = Column(Integer, nullable=False)
    foto = Column(BLOB, nullable=False)
    descricao = Column(VARCHAR(255), nullable=False)

    def __init__(self, id, nome, preco, qtd, foto, descricao):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.foto = foto
        self.descricao = descricao