from fastapi import FastAPI
from app.api.v1.endpoints import router as v1_router
from app.core.config import get_api_v1_str, get_project_name

app = FastAPI(title=get_project_name())
app.include_router(v1_router, prefix=get_api_v1_str(), tags=["v1"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="localhost", port=8000, log_level="info", reload=True)
# To run the application, use the command:
# uvicorn app.main:app --reload
# uvicorn app.main:app --host localhost --port 8000 --reload

