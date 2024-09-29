import uuid
from datetime import datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import JSONResponse
from database import add_video
from get_uuid import extract_uuid_from_link

app = FastAPI(
    title="Video Duplicate Checker API",
    version="1.0.0"
)

class VideoLinkRequest(BaseModel):
    link: str

class VideoLinkResponse(BaseModel):
    is_duplicate: bool
    duplicate_for: str

@app.post("/check-video-duplicate")
async def check_video_duplicate(video_link: VideoLinkRequest):

    upload_date = datetime.datetime.now()
    uuid_str = extract_uuid_from_link(video_link.link)
    add_video(UUID=uuid.UUID(uuid_str), upload_date=upload_date, isdupl=)
    response = VideoLinkResponse( is_duplicate=False, duplicate_for="0003d59f-89cb-4c5c-9156-6c5bc07c6fad")
    return response

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})