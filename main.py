from fastapi import FastAPI
from aplicativo import router

app = FastAPI()

app.include_router(router)
