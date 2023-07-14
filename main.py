from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user_router, naver_router

import os
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

origins = [
    os.getenv("API_SPRING_URL"),
    ## for live server
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router)
app.include_router(naver_router.router)