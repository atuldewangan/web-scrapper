from typing import Annotated

from fastapi import Header, HTTPException
from app.constant import STATIC_TOKEN


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != STATIC_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

