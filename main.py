from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

# title str, content str
class Post(BaseModel): 
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

#request type: GET method: root path URL: /
@app.get("/") # this is a decorator that tells the app to run the function below when the user goes to the root path
def root():
    return {"Welcome to my api!"}


@app.get("/posts") # this is a decorator that tells the app to run the function below when the user goes to the /posts path
def get_posts():
    return [
        {"title": "Post 1", "content": "This is the content of post 1"},
        {"title": "Post 2", "content": "This is the content of post 2"},
    ]

@app.post("/createposts") # this is a decorator that tells the app to run the function below when the user sends a POST request to the /posts path
def create_post(new_post: Post): # this function takes in a payload which is the body of the request
    print(new_post.title)
    return {"new_post": f"title: {new_post.title}, content: {new_post.content}, published: {new_post.published}, rating: {new_post.rating}"}