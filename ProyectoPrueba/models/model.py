from pydantic import BaseModel

class Users(BaseModel):
    nombre: str
    correo: str