from typing import Annotated

from fastapi import APIRouter, Form, status
from app.models import SignUpForm

router = APIRouter()

@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=SignUpForm)
async def sign_up(data: Annotated[SignUpForm, Form()]):
    return data