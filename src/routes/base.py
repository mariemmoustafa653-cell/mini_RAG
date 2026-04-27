from fastapi import FastAPI, APIRouter
import os
from helpers.config import get_settings 
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api/v1"],
)
@base_router.get("/")
async def welcome(): 
     app_settings = get_settings()
     app_name = app_settings.APP_NAME.value
     app_version = app_settings.app_version.value 
     return {"message": f"Welcome to {app_name} version {app_version}!"}