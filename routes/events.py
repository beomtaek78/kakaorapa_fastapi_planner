from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

events = []

# 모든 이벤트 출력
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events

# 특정 이벤트 출력
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="해당 ID 는 존재하지 않습니다"
    )

# 이벤트 생성
@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message": "새로운 이벤트가 생성되었습니다"
    }

# 단일 이벤트 삭제
@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message": "해당 이벤트가 삭제되었습니다"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="입력한 ID가 존재하지 않습니다"
    )

# 전체 이벤트 삭제
@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "모든 이벤트가 삭제되었습니다"
    }