from conexao import *
from models import *
from sqlalchemy.orm import joinedload

def consultar_alunos_db():
    with session:
        alunos = session.query(Aluno).all()
    return alunos

def consultar_alunos_info_db():
    with session:
        alunos = session.query(Aluno).options(joinedload(Aluno.endereco),
                                              joinedload(Aluno.email),
                                              joinedload(Aluno.disciplina)).all()
    return alunos

def consultar_disciplinas_db():
    with session:
        disciplinas = session.query(Disciplina).all()
        return disciplinas


    # try:
    #     session = conectar()
    #     alunos = session.query(Aluno).all()
    # except Exception as ex:
    #     print(ex)
    # finally:
    #     desconectar(session)
        
    # return alunos