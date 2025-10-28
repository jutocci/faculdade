from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "aluno"

    id_aluno = Column(Integer, primary_key=True)
    nome  = Column(String)

    def __init__(self, id, nome):
        self.id_aluno = id
        self.nome = nome

    def __str__(self):
        return str(self.id_aluno) + " " + self.nome


class Endereco(Base):
    __tablename__ = "endereco"

    id_endereco = Column(Integer, primary_key=True)
    rua  = Column(String)
    id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'))
    aluno = relationship("Aluno", back_populates="endereco")

    def __init__(self, id, rua):
        self.id_endereco = id
        self.rua = rua

    def __str__(self):
        return str(self.id_endereco) + " " + self.rua

