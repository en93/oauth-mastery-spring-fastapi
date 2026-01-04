from typing import Annotated

from fastapi import APIRouter, Form, status, Depends
from app.models import SignUpForm
from app.utilities.dependencies import get_session
from app.services.sign_up_service import sign_up

router = APIRouter()


@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=SignUpForm)
async def sign_up_route(sign_up_form: Annotated[SignUpForm, Form()], session = Depends(get_session)):
    return await sign_up(sign_up_form, session)
