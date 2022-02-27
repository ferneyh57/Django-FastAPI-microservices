from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from fastapi.security import OAuth2PasswordBearer

JWT_SECRET = 'myjwtsecret'

app = FastAPI()
db_url = 'sqlite:///db.sqlite3'
# register_tortoise(
#   app, 
#   db_url=db_url,
#   modules={'models': ["app.user.model"]},
#   generate_schemas=True,
#   add_exception_handlers=True
# )
#TODO: Revisar la ruta del modelo
async def init():
  await Tortoise.init(db_url=db_url, modules={'models': [".user.model"]})
  await Tortoise.generate_schemas()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


from app.admin import routes
from app.user import routes