from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uvicorn

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="public"), name="static")

# Templates
templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    with open("index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/signup")
async def signup(
    name: str = Form(...),
    email: str = Form(...),
    company: str = Form(...),
    role: str = Form(...)
):
    # Here you would typically save the data to a database
    # For now, we'll just print it
    print(f"New signup: {name} ({email}) from {company} as {role}")
    return {"status": "success", "message": "Thank you for your interest! We will contact you soon."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 