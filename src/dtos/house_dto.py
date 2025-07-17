from pydantic import BaseModel


class HousePredictDto(BaseModel):
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