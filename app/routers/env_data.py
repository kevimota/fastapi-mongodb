from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException
from ..dependencies import env_data_col
from ..models.env_data import EnvDataModel, UpdateEnvDataModel

router = APIRouter(
    prefix="/env_data",
    tags=["env_data"],
)


@router.get("/", response_model=EnvDataModel)
async def get_last_env_data():
    data = await env_data_col.find_one({}, sort=[("timestamp", -1)])
    return data


@router.post("/")
async def create_env_data(new_data: UpdateEnvDataModel):
    try:
        new_data.timestamp = datetime.now(timezone.utc)
        answer = await env_data_col.insert_one(dict(new_data))
        return {"status_code": 200, "id": str(answer.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
