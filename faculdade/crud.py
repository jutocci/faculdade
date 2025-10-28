from crud_db import *

def consultar_alunos():
    alunos = consultar_alunos_db()

    if not alunos:
        print("Nenhum aluno encontrado.")
        return
    else:
        for aluno in alunos:
            print(aluno)
            print(aluno.endereco)