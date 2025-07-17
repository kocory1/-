from src.dtos.house_dto import HousePredictDto
from fastapi import APIRouter
from src.services.house import runModel
from pydantic import BaseModel
from src.services.house import runModel2

class HouseBodyDto(BaseModel):
    crim: float
    room: float
    zn: float
    indus: float
    chas: float
    nox: float
    age: float
    dis: float
    rad: float
    tax: float
    ptratio: float
    b: float
    lstat: float
    
    
house_router = router = APIRouter()

@router.post("/price/predict")
async def get_house(crim : float, room:float):
    result = await runModel(crim, room)
    return {"price": result}

@router.post("/price/predict2")
async def get_house2(body: HousePredictDto):
    
    
    result = await runModel2(body)
    
    return {"price": result}
    