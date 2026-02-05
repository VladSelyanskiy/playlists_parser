import logging

import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse

from src.config import conf_static

# Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(content=open(conf_static.PATH_HTML, "r").read())


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(conf_static.PATH_FAVICON)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


@app.post("/submit")
async def get_status(input_url: str = Form(...)):
    logger.info(f"Received URL: {input_url}")
    return {"url": input_url}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
