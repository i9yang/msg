from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from app import crud
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return RedirectResponse(url="/items/")

@app.get("/items/", response_class=HTMLResponse)
async def get(request: Request):
    messages = crud.get()
    return templates.TemplateResponse(request=request, name="item.html", context={"msg" : messages})
