from app import app
from .model import Admin
from tortoise.contrib.pydantic import pydantic_model_creator
from passlib.hash import bcrypt

@app.get("/")
async def root():
  # user_obj = Users(
  #   username="contruto", 
  #   name="daniel", 
  #   surname="clavijo", 
  #   password_hash=bcrypt.hash("secret"),
  # )
  #TODO: no funciona
  user_obj = Admin.create(
    name="daniel"
  )
  #await user_obj.save()
  #return await User_Pydantic.from_tortoise_orm(user)
  #user = await Users.create(username="contruto", name="daniel", surname="clavijo", password_hash="secret")
  #print(user.all().values("id", "name"))
  return "user_obj"
