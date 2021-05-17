from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def respond():
    return{"This is no goods."}

@app.get("/about")
def about():
    return{
        'data':{ 'name':'This is a about page.'}
    } 
    

@app.get("/blog")
def home():
    return {
             'data':'blog list'
            }


# fetching blog of certain id.

@app.get("/blog/{id}")
def show(id):
    #fetch blog id.
    return {
             'data':id
            }
#fetch comments fo the certain blog dynamic

@app.get("/blog/{id}/comments")
def comments(id):
    #fetch comments for the blog id = id

    return{'data': {'1','2'}}