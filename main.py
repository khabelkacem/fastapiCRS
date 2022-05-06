from fastapi import FastAPI, Response, Request, Form
from predict import fastapi_RSC
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn




app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory=".")

class CourseModel(BaseModel):
    index: int
    Title: str
    Summary: str
    Enrollment: int
    Stars: float
    Rating: int
    Link: str

@app.get("/title")
def pong():
    return fastapi_RSC('HTML and CSS: A Guide to Web Design')

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/getCourses/{title}")
async def getCourses(request: Request, title: str ):
    result = fastapi_RSC(title)
    return templates.TemplateResponse('course.html', context={'request': request, 'result': result})


@app.get("/recommand/{title}")
async def recommand(title):
    return fastapi_RSC(title)
   

@app.post("/formSubmit")
async def form_post(request: Request,title: str = Form(...)):
        result = fastapi_RSC(title)
        return templates.TemplateResponse('index.html', context={'request': request, 'result': result})
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)
    