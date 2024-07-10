# FastAPI Accelerator
Python FastAPI Accelerator


## 🔩 Requirements

- Python
- FastAPI
- Docker
- Postgres


## 🟢 Initiate
To start using or developing, install the necessary libraries using the commands:


* Create venv
    ```
    python -m venv .venv
    ```

* Install libs
    ```
    pip install -r .\requirements.txt
    ```

* Initialize venv
    ```
    .\.venv\Scripts\activate
    ```


## ⚙️ Env Parameters

To initiate API service, the archive `.env` must be fill, like below:

[.env](/.env)
```
APP_CONTAINER_NAME=api_app                                         # [string] App conatiner name
FASTAPI_APP=main:app                                              # [string] Main route
FASTAPI_HOST=0.0.0.0                                              # [string] IP address
FASTAPI_PORT=8080                                                 # [int] Port number
FASTAPI_LOG_LEVEL=info                                            # [string] Log level fastapi parameter
FASTAPI_RELOAD=false                                              # [bool] Reloaded app fastapi parameter
FASTAPI_WORKERS=4                                                 # [int] Workers fastapi parameter
POSTGRES_DRIVERNAME=postgresql+asyncpg                             # [string] Database drivername 
POSTGRES_USER=postgres                                             # [string] Database username
POSTGRES_PASSWORD=postgres                                         # [string] Database user password
POSTGRES_HOST=api_db                                               # [string] Database address
POSTGRES_PORT=5432                                                 # [int] Database port number
POSTGRES_NAME=postgres                                             # [string] Database name
SECURITY_JWT_SECRET=X4NSg2eVgapaKspKHhp5MR23Z-HmshpZfMY_2L9oLQQ    # [string] JWT secret (create then with secrets *tutorial below*)
SECURITY_ALGORITHM=HS256                                           # [string] Secret algorithm
SECURITY_TOKEN_EXPIRE_MINUTES=60                                   # [int] Token expiration time (in minutes)
```


## 🔐 JWT Secret
To ensure user password security, create a JWT by following the steps below:
```
import secrets

token: str = secrets.token_urlsafe(32)
```


## 🧪 Tests

To test your API on root, upload a docker using the commands:
```
.\.venv\Scripts\activate
```
```
docker build -t dev-fastapi-accelerator .
```
```
docker run -d --env-file .env --name fastapi-accelerator -p 8000 dev-fastapi-accelerator
```
_the .env server file to register environment variables if necessary._

---

Or, tests through uvicorn itself:
```
.\.venv\Scripts\activate
```
```
python .\src\main.py    
```

---

To run tests from the `pytest` lib
```
pytest
```

```
pytest -q -m "<tags>" -c .\tests\pytest.ini
```


## ⚠️ Important

- Make sure all dependencies are installed correctly.


## 🤝 Colaborators

<table>
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/jo%C3%A3o-pedro-dias-caparroz-2b19a1161/" title="Linkedin Profile Icon">
        <img src="https://media.licdn.com/dms/image/C4D03AQHVyVT6CT6TFQ/profile-displayphoto-shrink_800_800/0/1595939105632?e=1724889600&v=beta&t=_pjNFXdW8VeM4IR5RhY9cgZ0NsAakg6EBEssgodCpwk" width="100px;" alt="Foto"/><br>
        <sub>
          <b>João Pedro Dias Caparroz</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## 😄 Contribute

To contribute [click here](/docs/CONTRIBUTING.md) | *not ready*
