from fastapi import APIRouter
from pydantic import BaseModel


class CreatePostBodyDto(BaseModel):
    height: int
    weight: int


user_router = router = APIRouter()


@router.get("/")
async def get_user(nickname: str, age: int):
    return {"nickname": nickname, "age": age}


@router.post("/{username}")
async def create_user(username : str, age : int, body: CreatePostBodyDto):
    height = body.height
    weight = body.weight
    processed_height = f"{height}cm"
    processed_weight = f"{weight}kg"
    
    
    return {"username": username, "age": age, "height": processed_height, "weight": processed_weight}
