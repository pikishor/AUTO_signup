from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uvicorn
from datetime import datetime
import json
import os

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
    try:
        # Create signups directory if it doesn't exist
        signups_dir = Path("signups")
        signups_dir.mkdir(exist_ok=True)
        
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format the signup data
        signup_data = {
            "timestamp": timestamp,
            "name": name,
            "email": email,
            "company": company,
            "role": role
        }
        
        # Append to signups.json file
        signups_file = signups_dir / "signups.json"
        existing_data = []
        
        if signups_file.exists():
            with open(signups_file, "r") as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []
        
        existing_data.append(signup_data)
        
        with open(signups_file, "w") as f:
            json.dump(existing_data, f, indent=2)
        
        return JSONResponse({
            "status": "success",
            "message": "Thank you for your interest! We will contact you soon."
        })
    except Exception as e:
        return JSONResponse({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }, status_code=500)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
