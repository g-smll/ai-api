from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import GetSessionListVO, BaseResponse

# 创建FastAPI应用实例
app = FastAPI(
    title="AI API",
    description="AI模型管理接口",
    version="1.0.0"
)

# 添加CORS中间件，允许跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 模拟数据库数据
mock_models = [
    {
        "id": 1,
        "category": "AI助手",
        "modelName": "deepseek",
        "modelDescribe": "DeepSeek大语言模型，具有强大的推理和代码生成能力",
        "modelPrice": 0.001,
        "modelType": "chat",
        "modelShow": "DeepSeek",
        "systemPrompt": "你是一个专业的AI助手，擅长推理、编程和问题解决。",
        "apiHost": "https://api.deepseek.com",
        "apiKey": "sk-xxx",
        "remark": "高性能推理模型，适合编程和复杂推理任务"
    }
]


@app.get("/api/system/model/modelList", response_model=BaseResponse[List[GetSessionListVO]])
async def get_models():
    """
    获取所有模型列表
    返回所有可用的AI模型信息
    """
    try:
        model_list = [GetSessionListVO(**model) for model in mock_models]
        return BaseResponse(
            code=200,
            data=model_list,
            msg="获取模型列表成功",
            rows=None
        )
    except Exception as e:
        return BaseResponse(
            code=500,
            data=None,
            msg=f"获取模型列表失败: {str(e)}",
            rows=None
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)