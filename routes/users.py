from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn
from database.connection import Database

user_router = APIRouter(
    tags=["User"],
)

user_database = Database(User)

users = {}

# 회원가입(등록)
@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="사용자가 이미 존재합니다"
        )
    await user_database.save(user)
    return {
        "message": "가입되었습니다"
    }

# 로그인
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 사용자입니다"
        )
    if user_exist.password == user.password:
        return {
            "message": "정상적으로 로그인 되었습니다"
        }
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="잘못된 패스워드입니다"
    )

