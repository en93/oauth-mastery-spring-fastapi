import asyncio
from functools import wraps
from typing import Callable, TypeVar, Awaitable, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")

def async_task(func: Callable[P, R]) -> Callable[P, Awaitable[R]]:
    """
    Decorator to run a synchronous function on the event loop
    without blocking it.
    """
    @wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return await asyncio.to_thread(func, *args, **kwargs)
    return wrapper