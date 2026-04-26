from fastapi import FastAPI, APIRouter

base_router = APIRouter()
@base_router.get("/welcome")
def welcome():  return {"message": "Welcome to all!"}