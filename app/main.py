from fastapi import FastAPI
from app.routes.shorten import router as shorten_router

app = FastAPI()

app.include_router(shorten_router)

@app.get("/")
def home():
    return {"message": "URL Shortener is running"}

from app.database import Base, engine
from app.models import URL

Base.metadata.create_all(bind=engine)
