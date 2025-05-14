from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uvicorn
from datetime import datetime

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
    # Create signups directory if it doesn't exist
    signups_dir = Path("signups")
    signups_dir.mkdir(exist_ok=True)
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Format the signup data
    signup_data = f"Timestamp: {timestamp}\nName: {name}\nEmail: {email}\nCompany: {company}\nRole: {role}\n{'='*50}\n"
    
    # Append to signups.txt file
    with open(signups_dir / "signups.txt", "a") as f:
        f.write(signup_data)
    
    return {"status": "success", "message": "Thank you for your interest! We will contact you soon."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
