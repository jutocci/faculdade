from conexao import *
from models import Aluno

def consultar_alunos_db():
    alunos = []

    try:
        session = conectar()
        alunos = session.query(Aluno).all()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)
        
    return alunos