from fastapi import FastAPI
from starlette.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

items = []

class post(BaseModel):
    id: str
    name: str
    

@app.get("/")
def index():
    return RedirectResponse(url="/docs/")

@app.get("/partes")
def get_root():
    return items

@app.post("/")
def post_root(post:post):
    return RedirectResponse(url="/docs/")

@app.put("/")
def put_root():
    return RedirectResponse(url="/docs/")

@app.delete("/")
def delete_root():
    return RedirectResponse(url="/docs/")

