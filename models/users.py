from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

# 사용자 모델
class User(BaseModel):
    email: EmailStr                 # 사용자 이메일
    password: str                   # 사용자 패스워드
    events: Optional[List[Event]]   # 사용자가 생성한 이벤트

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@test.pri",
                "password": "test123pwd",
                "events": [],
            }
        }

# 사용자 로그인 모델
class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@test.pri",
                "password": "test123pwd",
                "events": [],
            }
        }