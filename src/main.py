import logging

import uvicorn
from fastapi import FastAPI, Form, HTTPException, status
from fastapi.responses import FileResponse, HTMLResponse

from src.schemas.tracks_output import TracksOutput
from src.config import conf_static
from src.services.processing import get_data

# Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open(conf_static.PATH_HTML, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="HTML file not found")


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(conf_static.PATH_FAVICON)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


@app.post("/tracks")
async def get_tracks(input_url: str = Form(...)) -> TracksOutput:
    logger.info(f"Received URL: {input_url}")
    tracks_collection = get_data(input_url)
    if tracks_collection is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid URL or failed to fetch data",
        )
    output = TracksOutput(
        tracks=tracks_collection.tracks, playlist_data=tracks_collection.playlist_data
    )
    return output


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
