from fastapi import FastAPI
import uvicorn
from src.routers.index import index_router

# swagger 문서는 /docs 경로로, OpenApi 문서는 /open-api-docs 경로로 설정
app = FastAPI(docs_url="/docs",openapi_url="/open-api-docs")

# 추후에 라우터 붙이는 코드
app.include_router(index_router,prefix="/api")

@app.get("/")
async def getHello():
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="127.0.0.1",
        port=8080,
        reload=True,
        log_level="info"
    )

