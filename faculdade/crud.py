from crud_db import *

def consultar_alunos():
    alunos = consultar_alunos_db()

    if not alunos:
        print("Nenhum aluno encontrado.")
        return
    else:
        for aluno in alunos:
            print(aluno)
            #print(aluno.endereco)

def consultar_alunos_info():
    alunos = consultar_alunos_db()

    if not alunos:
        print("Nenhum aluno encontrado.")
        return
    else:
        for aluno in alunos:
            print(f"Aluno: {aluno.nome}")
            if aluno.endereco:
                print(f"Endereço: {aluno.endereco}")
            else:
                print("Endereço: Não cadastrado")

def consultar_disciplinas():
    disciplinas = consultar_disciplinas_db()

    if not disciplinas:
        print("Nenhuma disciplina encontrada.")
        return
    else:
        for disciplina in disciplinas:
            print(disciplina)