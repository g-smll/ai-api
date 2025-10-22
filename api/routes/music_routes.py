from fastapi import APIRouter, Query
from typing import List
from models import Album, Pagination, PageData, BaseResponse
from data.mock_albums import ALBUMS

router = APIRouter(prefix="/web/api/albums", tags=["Music"])

@router.get("", response_model=BaseResponse[PageData[Album]])
async def list_albums(page: int = Query(1, ge=1), size: int = Query(10, ge=1)):
    # 固定每页10条（如传入其他size则按10处理）
    size = 10
    total = len(ALBUMS)
    pages = (total + size - 1) // size
    if page > pages:
        page = pages if pages > 0 else 1
    start = (page - 1) * size
    end = start + size
    items = [Album(**a) for a in ALBUMS[start:end]]

    pagination = Pagination(page=page, size=size, total=total, pages=pages)
    data = PageData[Album](items=items, pagination=pagination)
    return BaseResponse(code=200, data=data, msg="获取专辑分页成功")