from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List
from app.dependencies import get_token_header
from app.models.databse import Database
from app.models.scrapper import Scraper
from app.services.notify_service import Notifier


router = APIRouter()
cache = {}

@router.post("/scrape/")
def scrape_data(num_pages: int = 1, proxy: str = None):
    scraper = Scraper(proxy)
    data = scraper.scrape(num_pages)
    db = Database()
    db.store_data(data)
    notifier = Notifier()
    notifier.notify(len(data))
    return {"message": f"{len(data)} products scraped and updated in the DB."}
