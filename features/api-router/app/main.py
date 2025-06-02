from fastapi import Depends, FastAPI
from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import user, post

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(user.user)
app.include_router(post.post)
app.include_router(
    admin.admin,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_query_token)],
    responses={418: {"description": "I'm a teapot"}}
)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Application"}
