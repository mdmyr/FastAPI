from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def respond():
    return{"This is no goods."}

@app.get("/about")
def about():
    return { "This is a about page."}

@app.get("/home")
def home():
    return {"Home Page"}
