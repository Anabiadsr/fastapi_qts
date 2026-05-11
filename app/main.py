from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def raiz():
    return{"mensagem" : "API FastAPI funcionando"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/soma")
def soma (a: int, b:int):
    return {"resultado": a + b}


# @app.get("/multiplicacao")
# def multiplicacao (a: int, b:int):
#     return {"resultado": a * b}

class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False

@app.post("/Tarefas")
def criar_tarefas(tarefa : Tarefa):
    return{
        "mensagem" : "Tarefa recebida com sucesso",

        "dados": tarefa
    }
   