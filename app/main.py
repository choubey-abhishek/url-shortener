from app.routes.redirect import router as redirect_router
from fastapi import FastAPI
from app.routes.shorten import router as shorten_router
from app.database import Base, engine

app = FastAPI()

if engine:
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print("DB error:", e)

app.include_router(shorten_router)

@app.get("/")
def home():
    return {"message": "URL Shortener is running"}
