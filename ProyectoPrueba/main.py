from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.model import Users


#App object
app = FastAPI()

from dataBase.database import (
    fetch_one_user,
    fetch_allusers,
    create_user,
    update_user,
    remove_user
)



origins = [
    'http://localhost:3000',
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message":"All Ok!"}

@app.get("/api/todo/{nombre}", response_model=Users)
async def get_user_by_id(nombre):
    response = await fetch_one_user(nombre)
    if response:
        return response
    raise HTTPException(404, f"usuario con nombre: {nombre} no existe")

@app.get("/api/todo")
async def get_users():
    response = await fetch_allusers()
    return response

@app.post("/api/todo", response_model=Users)
async def post_user(user: Users):
    response = await create_user(user.dict())
    if response:
        return response
    raise HTTPException(400, "Bad request")

@app.put("/api/todo{nombre}/", response_model=Users)
async def put_user(nombre:str, correo:str):
    response = await update_user(nombre, correo)
    if response:
        return response
    raise HTTPException(404, f"no existe nombre de usuario: {nombre}")

@app.delete("/api/todo/{nombre}")
async def delete_user(nombre):
    response = await remove_user(nombre)
    #print(response,"<=== response")
    if response:
        return "Usuario Eliminado Correctamente"
    raise HTTPException(404, f"usuario: {nombre} no encontrado")
    