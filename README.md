# AI API 服务

一个基于 FastAPI 的 AI 模型管理接口服务，提供模型列表查询功能。

## 项目简介

本项目提供了一个简洁的 AI 模型管理 API，支持获取模型列表信息。当前集成了 DeepSeek 大语言模型，API 返回格式符合统一的 BaseResponse 规范，便于前端集成使用。

## 技术栈

- **Python**: 3.12+
- **FastAPI**: 高性能 Web 框架
- **Pydantic**: 数据验证和序列化
- **Uvicorn**: ASGI 服务器

## 项目结构

```
ai-api/
├── main.py          # FastAPI 主应用
├── models.py        # 数据模型定义
├── requirements.txt # 项目依赖
├── test_api.py     # API 测试脚本
└── README.md       # 项目文档
```

## 安装和运行

### 1. 环境准备

确保已安装 Python 3.12+ 和 conda/pip 包管理器。

### 2. 创建虚拟环境（推荐）

```bash
# 使用 conda 创建虚拟环境
conda create -n ai-api python=3.12
conda activate ai-api

# 或使用 venv 创建虚拟环境
python -m venv ai-api
# Windows
ai-api\Scripts\activate
# Linux/Mac
source ai-api/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 启动服务

```bash
# 开发模式启动（支持热重载）
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 生产模式启动
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 5. 验证服务

服务启动后，可以通过以下方式验证：

- **API 文档**: http://localhost:8000/docs
- **API 接口**: http://localhost:8000/system/model/modelList
- **运行测试**: `python test_api.py`

## API 接口

### 获取模型列表

**接口地址**: `GET /system/model/modelList`

**响应格式**:
```json
{
  "code": 200,
  "data": [
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
  ],
  "msg": "获取模型列表成功"
}
```

**字段说明**:
- `code`: 响应状态码（200 成功，500 失败）
- `data`: 模型列表数据
- `msg`: 响应消息

**模型对象字段**:
- `id`: 模型唯一标识
- `category`: 模型分类
- `modelName`: 模型名称
- `modelDescribe`: 模型描述
- `modelPrice`: 模型价格
- `modelType`: 模型类型
- `modelShow`: 显示名称
- `systemPrompt`: 系统提示词
- `apiHost`: API 主机地址
- `apiKey`: API 密钥
- `remark`: 备注信息

## 开发说明

### 添加新模型

在 `main.py` 的 `mock_models` 列表中添加新的模型数据：

```python
{
    "id": 2,
    "category": "AI助手",
    "modelName": "gpt-4",
    "modelDescribe": "OpenAI GPT-4模型，具有强大的理解和生成能力",
    "modelPrice": 0.03,
    "modelType": "chat",
    "modelShow": "GPT-4",
    "systemPrompt": "你是一个有用的AI助手，请提供准确和有帮助的回答。",
    "apiHost": "https://api.openai.com",
    "apiKey": "sk-your-openai-key",
    "remark": "高质量对话模型，适合复杂任务"
}
```

### 修改响应格式

如需修改响应格式，请编辑 `models.py` 中的 `BaseResponse` 类。

### 运行测试

```bash
python test_api.py
```

## 部署

### Docker 部署（可选）

创建 `Dockerfile`:
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

构建和运行：
```bash
docker build -t ai-api .
docker run -p 8000:8000 ai-api
```

## 常见问题

### Q: 如何修改端口？
A: 在启动命令中修改 `--port` 参数，例如：`uvicorn main:app --reload --host 0.0.0.0 --port 9000`

### Q: 如何添加 HTTPS 支持？
A: 使用 `--ssl-keyfile` 和 `--ssl-certfile` 参数，或在前端代理（如 Nginx）中配置 SSL。

### Q: 如何连接真实数据库？
A: 修改 `main.py` 中的 `mock_models`，替换为数据库查询逻辑。

## 许可证

MIT License

## 联系方式

如有问题或建议，请联系项目维护者。