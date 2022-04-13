from models.model import Users

#Controlador MongoDb
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.users
collection = database.empleados


async def fetch_one_user(nombre):
    document = await collection.find_one({"nombre": nombre})
    return document

async def fetch_allusers():
    users = []
    cursor = collection.find({})
    async for document in cursor:
        users.append(Users(**document))
    return  users

async def create_user(user):
    document = user
    result = await collection.insert_one(document)
    return document

async def update_user(nombre, correo):
    await collection.update_one({"nombre":nombre}, {"$set":{
        "correo":correo}})
    document = await collection.find_one({"nombre":nombre})
    return document

async def remove_user(nombre):
    response = await collection.delete_one({"nombre":nombre})
    return True