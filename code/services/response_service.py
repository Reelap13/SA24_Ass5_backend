from fastapi import HTTPException
from fastapi.responses import JSONResponse
from typing import Callable, Any
from schemas.response_models import ResponseData

async def handle_request(func: Callable[..., ResponseData]) -> JSONResponse:
    try:
        response_data: ResponseData = await func()
        return JSONResponse(status_code=response_data.code, content=response_data.dict()) 
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))
