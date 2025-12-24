from fastapi import FastAPI
from app.routes.sign_up_route import router as sign_up_router
from app.routes.hello_world import router as hello_router

app = FastAPI()

app.include_router(sign_up_router)
app.include_router(hello_router)
