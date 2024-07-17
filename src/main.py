from fastapi import FastAPI

from core.config import settings
from api.v1.api import router
from utils import get_env_fastapi_config
from create_tables import create_tables


app = FastAPI(title='FastAPI-Accelerator')
app.include_router(router, prefix=settings.API_VERSION_ADDRESS)


if __name__ == '__main__':
    import uvicorn
    import asyncio

    asyncio.run(create_tables())
    uvicorn.run(**get_env_fastapi_config())

