from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routes.user_creation_route import router as user_creation_route
from app.routes.hello_world import router as hello_router
import logging
from app.utilities.database import create_session_factory
from app.settings import app_settings

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  # todo customize this


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    app.state.session_factory = create_session_factory(app_settings)
    yield
    app.state.session_factory = None


app = FastAPI(lifespan=lifespan)

app.include_router(user_creation_route)
app.include_router(hello_router)
