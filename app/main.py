from fastapi import FastAPI
from app.database import engine, Base
from app.models import Course, Lead 
from app.routes.courses import router as course_router

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind = engine)

app = FastAPI(
    title="AdmitFlow AI",
    description="AI-powered Admission assistant for coaching institutes",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)
app.include_router(course_router)

@app.get("/")
def home():
    return{
        "message": "Welcome to AdmitFlow AI",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {
        "status" : "healthy"
    }
