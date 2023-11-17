from fastapi import FastAPI

from routers import micro_searchr


app = FastAPI()

app.include_router(micro_searchr.router)
