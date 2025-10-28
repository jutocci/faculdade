import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BANCO = "infnet.db"
DIR = os.path.dirname(os.path.abspath(__file__))
BANCO = os.path.join(DIR, BANCO)

def conectar():
    session = None
    try:
        engine = create_engine("sqlite:///" + BANCO)
        session = sessionmaker(bind = engine)()
    except Exception as ex:
        print(ex)
    return session

def desconectar(session):
    if session:
        session.close()

session = conectar()
desconectar(session)
