from typing import Annotated

from fastapi import Header, HTTPException

STATIC_TOKEN = "your_static_token_here"

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != STATIC_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

