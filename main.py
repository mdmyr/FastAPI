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
    

##fetching limited query, like passing a parameter to the query.
## positioning matters

@app.get("/blog")
def getblog(limit):
    #F is used to substitubte the parameter
    return {'data': f'{limit} of the logs'}



@app.get("/blog")
def home():
    return {
             'data':'blog list'
            }

#fetch unpublshed the blogs
@app.get("/blog/unpublished")
def unpublished():
    #fetch the unpublished
    return {'data':'Get the published blogs'}






# fetching blog of certain id.
#making the id as integer 
@app.get("/blog/{id}")
def show(id : int):
    #fetch blog id.
    return {
             'data':id
            }
#fetch comments fo the certain blog dynamic

@app.get("/blog/{id}/comments")
def comments(id):
    #fetch comments for the blog id = id

    return{'data': {'1','2'}}