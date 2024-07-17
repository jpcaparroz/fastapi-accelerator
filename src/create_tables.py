from sqlalchemy import inspect

from core.config import settings
from core.database import engine


def check_table_exists(conn) -> bool:
    inspector = inspect(conn)
    existing_tables = inspector.get_table_names()
    tables_to_create = settings.DBBaseModel.metadata.tables.keys()
    return not all(table in existing_tables for table in tables_to_create)


async def create_tables() -> None:
    import models.__all_models
    print('Creating database tables...')
    
    async with engine.begin() as conn:
        table_exists = await conn.run_sync(check_table_exists)
        if table_exists:
            await conn.run_sync(settings.DBBaseModel.metadata.create_all)
            print('Table creation successfully')
        else:
            print('Tables already exists')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())

