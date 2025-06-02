from fastapi import APIRouter

admin = APIRouter()

@admin.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}