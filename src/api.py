from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.settings import Settings
from v1 import v1_router

settings = Settings()

app = FastAPI(title="RootServer")
app.include_router(v1_router)
app.mount(path='/', app=StaticFiles(directory=str(settings.webapp_static_path)), name="webapp")


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass
