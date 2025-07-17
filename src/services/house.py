from typing import List
import xgboost as xgb
import pandas as pd
from src.dtos.house_dto import HousePredictDto


loaded_model = xgb.XGBRegressor()

loaded_model.load_model("models/xgb_model.json")


async def runModel(crim: float, room: float) -> List[float]:

    dic = {
        "CRIM": [crim],
        "ZN": [18.0],
        "INDUS": [22.37],
        "CHAS": [0],
        "NOX": [0.145],
        "RM": [room],
        "AGE": [66.7],
        "DIS": [4.291],
        "RAD": [13],
        "TAX": [333.333],
        "PTRATIO": [21.0],
        "B": [197.6],
        "LSTAT": [23.4],
    }

    input = pd.DataFrame.from_dict(dic, orient='columns')

    z = loaded_model.predict(input)

    result: List[float] = z.tolist()

    return result

async def runModel2(dto: HousePredictDto) -> List[float]:
    dic = {
        "CRIM": [dto.crim],
        "ZN": [dto.zn],
        "INDUS": [dto.indus],
        "CHAS": [dto.chas],
        "NOX": [dto.nox],
        "RM": [dto.room],
        "AGE": [dto.age],
        "DIS": [dto.dis],
        "RAD": [dto.rad],
        "TAX": [dto.tax],
        "PTRATIO": [dto.ptratio],
        "B": [dto.b],
        "LSTAT": [dto.lstat],
    }

    input = pd.DataFrame.from_dict(dic, orient='columns')

    z = loaded_model.predict(input)

    result: List[float] = z.tolist()

    return result
