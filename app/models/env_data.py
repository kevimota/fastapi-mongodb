from datetime import datetime, timezone
from typing import Optional, List
from pydantic import BaseModel, Field
from .object_id import PyObjectId

class EnvDataModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    pressure: float
    temperature: float
    humidity: float
    timestamp: datetime = datetime.now(timezone.utc)
    
class UpdateEnvDataModel(BaseModel):

    name: str
    pressure: float
    temperature: float
    humidity: float
    timestamp: datetime = datetime.now(timezone.utc)


class EnvDataCollection(BaseModel):

    data: List[EnvDataModel]