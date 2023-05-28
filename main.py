from fastapi import FastAPI
from routes.users import user_router

import uvicorn

# FastAPI() 인스턴스 생성후 앞서 정의한 라우트 등록
app = FastAPI()
app.include_router(user_router, prefix="/user")

# uvicorn.run() 메서드 이용하여 8000 포트에서 애플리케이션 실행
if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
