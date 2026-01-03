from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from app.database import SessionLocal
from app.models import URL

router = APIRouter()

@router.get("/{short_code}")
def redirect_url(short_code: str):
    db = SessionLocal()
    url = db.query(URL).filter(URL.short_code == short_code).first()
    db.close()

    if not url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url.long_url)
