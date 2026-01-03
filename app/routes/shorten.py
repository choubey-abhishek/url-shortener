from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import string
import random
from app.database import SessionLocal
from app.models import URL

router = APIRouter(prefix="/api/v1")

class URLRequest(BaseModel):
    long_url: str

def generate_short_code(length=6):
    """Generate a random short code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@router.post("/shorten")
def create_short_url(request: URLRequest):
    db = SessionLocal()

    # Ensure unique short code
    while True:
        code = generate_short_code()
        existing = db.query(URL).filter(URL.short_code == code).first()
        if not existing:
            break

    new_url = URL(long_url=request.long_url, short_code=code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    db.close()

    # Construct the live short URL (use your deployed Railway domain)
    short_url = f"https://url-shortener-production-4c07.up.railway.app/{new_url.short_code}"

    return {"short_url": short_url}
