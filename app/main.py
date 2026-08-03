from fastapi import FastAPI
from app.api.users import router as users_router

app = FastAPI(
    title="Senior SRE Tech Challenge",
    version="1.0.0"
)

app.include_router(users_router)

@app.get("/")
def root():
    return {
        "application": "senior-sre-tech-challenge",
        "status": "running"
    }


@app.get("/health/live")
def health_live():
    return {
        "status": "ok"
    }


@app.get("/health/ready")
def health_ready():
    return {
        "status": "ready"
    }