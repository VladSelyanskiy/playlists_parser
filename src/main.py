from fastapi import FastAPI, Form
import uvicorn
from fastapi.responses import HTMLResponse, FileResponse
from config import config

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(content=open(config.PATH_HTML, "r").read())


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(config.PATH_FAVICON)


@app.post("/submit")
async def get_status(input_url: str = Form(...)):
    return {"url": input_url}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
