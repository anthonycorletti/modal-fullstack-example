from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import env, log

app = FastAPI()
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def _index(request: Request) -> Response:
    log.info(f"whoa! the secret is {env.API_SECRET_KEY}")
    return templates.TemplateResponse(name="index.html", context={"request": request})
