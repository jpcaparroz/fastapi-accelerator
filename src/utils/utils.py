import os
from pathlib import Path

from sqlalchemy import URL

from strtobool import strtobool

from dotenv import load_dotenv


ENV_PATH = Path(f'{os.getcwd()}/.env')
load_dotenv(dotenv_path=ENV_PATH, override=True)


def get_env(env_name: str) -> str:
    return os.getenv(env_name)


def get_db_url() -> str:
    drivername: str = os.getenv('POSTGRES_DRIVERNAME')
    username: str = os.getenv('POSTGRES_USER')
    password: str = os.getenv('POSTGRES_PASSWORD')
    host: str = os.getenv('POSTGRES_HOST')
    port: int = int(os.getenv('POSTGRES_PORT'))
    database: str = os.getenv('POSTGRES_NAME')

    if "INSTANCE_UNIX_SOCKET" in os.environ:
        unix_socket_path = os.environ.get("INSTANCE_UNIX_SOCKET")
        print("*************************************")
        print(f"{drivername}://{username}:{password}@/{database}?unix_sock={unix_socket_path}/.s.PGSQL.5432")
        print("*************************************")
        return f"{drivername}://{username}:{password}@/{database}?unix_sock={unix_socket_path}/.s.PGSQL.5432"
    else:
        config = {
            "drivername": drivername,
            "username": username,
            "password": password,
            "host": host,
            "port": port,
            "database": database
        }
        print("*************************************")
        print(config)
        print("*************************************")
        return URL.create(**config).render_as_string(hide_password=False)


def get_env_fastapi_config() -> dict:
    config = {
        "app": os.getenv('FASTAPI_APP'),
        "host": os.getenv('FASTAPI_HOST'),
        "port": int(os.getenv('FASTAPI_PORT')),
        "log_level": os.getenv('FASTAPI_LOG_LEVEL'),
        "reload": strtobool(os.getenv('FASTAPI_RELOAD')),
        "workers": int(os.getenv('FASTAPI_WORKERS'))
    }
    print("*************************************")
    print(config)
    print("*************************************")
    return config

