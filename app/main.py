from fastapi import FastAPI

app = FastAPI(
    title="Senior SRE Tech Challenge",
    version="1.0.0"
)


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