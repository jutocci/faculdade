from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "aluno"

    id_aluno = Column(Integer, primary_key=True)
    nome  = Column(String)
    endereco = relationship("Endereco", uselist=False, back_populates="aluno")
    email = relationship("Email", cascade="all, delete")
    disciplina = relationship("Disciplina", secondary="aluno_disciplina", back_populates="aluno")

    def __init__(self, id, nome):
        self.id_aluno = id
        self.nome = nome

    def __str__(self):
        return str(self.id_aluno) + " " + self.nome


class Endereco(Base):
    __tablename__ = "endereco"

    id_endereco = Column(Integer, primary_key=True)
    rua  = Column(String)
    id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'), unique=True)
    aluno = relationship("Aluno", back_populates="endereco")

    def __init__(self, id, rua):
        self.id_endereco = id
        self.rua = rua

    def __str__(self):
        return str(self.id_endereco) + " " + self.rua


class Email(Base):
    __tablename__ = "email"

    id_email = Column(Integer, primary_key=True)
    email  = Column(String)
    id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'))
    aluno = relationship("Aluno", back_populates="email")

    def __init__(self, id, email):
        self.id_email = id
        self.email = email

    def __str__(self):
        return str(self.id_email) + " " + self.email
    
class Disciplina(Base):
    __tablename__ = "disciplina"

    id_disciplina = Column(Integer, primary_key=True)
    nome  = Column(String)
    aluno = relationship("Aluno", secondary="aluno_disciplina", back_populates="disciplina")

    def __init__(self, id, nome):
        self.id_disciplina = id
        self.nome = nome

    def __str__(self):
        return f"{self.id_disciplina} {self.nome}"
    

class AlunoDisciplina(Base):
    __tablename__ = "aluno_disciplina"

    id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'), primary_key=True)
    id_disciplina = Column(Integer, ForeignKey('disciplina.id_disciplina'), primary_key=True)

    def __init__(self, id_aluno, id_disciplina):
        self.id_aluno = id_aluno
        self.id_disciplina = id_disciplina
    
    def __str__(self):
        return f"Aluno ID: {self.id_aluno}, Disciplina ID: {self.id_disciplina}"
    
