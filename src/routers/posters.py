from fastapi import APIRouter
from typing import Optional

posters_router = router = APIRouter()


@router.get("/{number}")
async def get_user(number: int, content: Optional[str] = None, isArticle: bool = False):
    return {"message" : f"{number} 번째 포스트입니다.", "content" : content,
            "isArticle": isArticle}
    
