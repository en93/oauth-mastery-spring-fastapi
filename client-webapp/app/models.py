from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel


class SignUpForm(BaseModel):
    username: str
    email: str
    password: str
    greeting: str


