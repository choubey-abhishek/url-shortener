from fastapi import APIRouter
from app.schemas import ShortenURLRequest, ShortenURLResponse
from app.services.short_code import generate_short_code

router = APIRouter(prefix="/api/v1")

@router.post("/shorten", response_model=ShortenURLResponse)
def shorten_url(request: ShortenURLRequest):
    short_code = generate_short_code()
    short_url = f"http://localhost:8000/{short_code}"
    return ShortenURLResponse(short_url=short_url)
