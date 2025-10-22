from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.model_routes import router as model_router
from api.routes.music_routes import router as music_router

app = FastAPI(
    title="AI API",
    description="AI模型管理接口",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(model_router)
app.include_router(music_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)