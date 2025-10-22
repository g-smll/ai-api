from fastapi import APIRouter
from typing import List
from models import GetSessionListVO, BaseResponse
from data.mock_models import MOCK_MODELS

router = APIRouter(prefix="/web/api/models", tags=["Model"])

@router.get("", response_model=BaseResponse[List[GetSessionListVO]])
async def get_models():
    model_list = [GetSessionListVO(**m) for m in MOCK_MODELS]
    return BaseResponse(code=200, data=model_list, msg="获取模型列表成功")