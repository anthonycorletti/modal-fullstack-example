from pathlib import Path

import modal
from fastapi import FastAPI

from app._env import _Env
from app.main import app

stub = modal.Stub()

stub["env"] = modal.Secret(_Env(_env_file=".env").dict())

image = modal.Image.debian_slim().pip_install(
    [
        "fastapi>=0.70.0",
        "python-dotenv>=0.21.0",
        "structlog>=21.2.0",
        "jinja2>=3.1.2",
    ]
)

parent = Path(__file__).parent.parent
static_path = parent / "static"
templates_path = parent / "templates"


@stub.asgi(
    image=image,
    secret=stub["env"],
    mounts=[
        modal.Mount("/root/static", local_dir=static_path),
        modal.Mount("/root/templates", local_dir=templates_path),
    ],
)
def _app() -> FastAPI:
    return app


if __name__ == "__main__":
    stub.serve()
