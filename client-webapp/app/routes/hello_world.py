from fastapi import APIRouter

router = APIRouter()


@router.post("/hello")
async def root():
    return {"message": "Hello World"}
