from fastapi import Depends, FastAPI
import uvicorn
from app.routers import scrapper
from app.dependencies import get_token_header


app = FastAPI(dependencies=[Depends(get_token_header)],)
app.include_router(scrapper.router)


@app.get("/")
async def root():
    return {"message": "Scrapper is rurnning!"}
