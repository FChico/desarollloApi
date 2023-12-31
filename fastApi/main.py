from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", 
             "content": "content of post 1", "id": 1}, 
            {"title": "favorite foods", 
             "content": "I like pizza", "id": 2}] 


def find_posts(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
            
@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts} 

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000)
    my_posts.append(post_dict)
    return {"data": my_posts}



@app.get("/posts/latest")
async def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}


@app.get("/posts/{id}")
async def get_post(id: int, response: Response):
    post = find_posts(id)
    
    if not post:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"post with id: {id} was not found" 
        )
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message": f"post with id: {id} was not found"}
    return {"post_detail": post}

@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    # find the index in the array that has required ID
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"post with id: {id} does not exist"
        )
        
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
async def update_posts(id: int, post: Post):
    return {"message": "update post"}