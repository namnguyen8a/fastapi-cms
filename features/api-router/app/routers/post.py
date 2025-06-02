from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

post = APIRouter(
    prefix="/posts",
    tags=["posts"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
)

fake_posts_db = {
    "person 1":{
        "post_id": 0,
        "post_content": "Hehe",
    },
    "person 2":{
        "post_id": 1,
        "post_content": "haha",
    },
}

@post.get("/")
async def read_posts():
    return fake_posts_db

@post.get("/{person_id}")
async def read_person_post(person_id: str):
    if person_id not in fake_posts_db:
        raise HTTPException(status_code=404, detail="Posts not found")
    return {"content": fake_posts_db[person_id]["post_content"], "person_id": person_id}

@post.put(
    "/{person_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_person_posts(person_id: str):
    if person_id != "person 1":
        raise HTTPException(
            status_code=403, detail="You can only update the post by person 1"
        )
    return {"person_id": person_id, "post": "post by person 1"}