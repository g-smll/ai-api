from pydantic import BaseModel
from typing import Optional, List, Generic, TypeVar

# 定义泛型类型变量
T = TypeVar('T')


class GetSessionListVO(BaseModel):
    """
    会话列表视图对象模型
    对应前端的GetSessionListVO接口
    """
    id: Optional[int] = None
    category: Optional[str] = None
    modelName: Optional[str] = None
    modelDescribe: Optional[str] = None
    modelPrice: Optional[float] = None
    modelType: Optional[str] = None
    modelShow: Optional[str] = None
    systemPrompt: Optional[str] = None
    apiHost: Optional[str] = None
    apiKey: Optional[str] = None
    remark: Optional[str] = None

    class Config:
        # 允许字段别名
        allow_population_by_field_name = True
        # 示例数据
        schema_extra = {
            "example": {
                "id": 1,
                "category": "AI助手",
                "modelName": "GPT-4",
                "modelDescribe": "OpenAI最新的大语言模型",
                "modelPrice": 0.03,
                "modelType": "chat",
                "modelShow": "GPT-4",
                "systemPrompt": "你是一个有用的AI助手",
                "apiHost": "https://api.openai.com",
                "apiKey": "sk-xxx",
                "remark": "高质量对话模型"
            }
        }


class BaseResponse(BaseModel, Generic[T]):
    """
    统一响应格式模型
    对应前端的BaseResponse接口
    """
    code: int
    data: Optional[T] = None
    msg: str
    rows: Optional[T] = None

    class Config:
        schema_extra = {
            "example": {
                "code": 200,
                "data": None,
                "msg": "操作成功",
                "rows": []
            }
        }