from pydantic import BaseModel
from typing import Any

class ResponseData(BaseModel):
    code: int
    message: str
    data: Any
