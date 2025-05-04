from fastapi import FastAPI
from api.user_api import router as user_router

app = FastAPI(title="Online Appointment Scheduler")

app.include_router(user_router)

@app.get("/")
def root():
    return {"status": "running"}
