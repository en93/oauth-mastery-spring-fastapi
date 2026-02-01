from typing import Annotated

from fastapi import APIRouter, Form, status, Depends
from app.models.user_creation import user_creation
from app.utilities.dependencies import get_session
from app.services.user_creation_service import create_user

router = APIRouter()


@router.post(
    "/sign-up", status_code=status.HTTP_201_CREATED, response_model=user_creation
)
async def user_creation_route(
    sign_up_form: Annotated[user_creation, Form()], session=Depends(get_session)
):
    await create_user(sign_up_form, session)
    return sign_up_form
