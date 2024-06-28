from fastapi import FastAPI

from core.config import settings
from api.v1.api import router
from utils import get_config

app = FastAPI(title='FastAPI-Accelerator')
app.include_router(router, prefix=settings.API_VERSION_ADDRESS)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(**get_config('server'))

