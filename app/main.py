from fastapi import FastAPI
from app.routes.shorten import router as shorten_router

app = FastAPI()

app.include_router(shorten_router)

@app.get("/")
def home():
    return {"message": "URL Shortener is running"}
