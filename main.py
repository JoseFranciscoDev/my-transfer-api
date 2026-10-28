from fastapi import FastAPI

from api.v1.files_router import router as files_router

app = FastAPI()

app.include_router(files_router)
