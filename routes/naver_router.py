from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from login import login_naver
import requests
import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter(
    prefix="/naver",
)


@router.get("/login")
def login():
    url = login_naver.login()
    response = RedirectResponse(url=url)
    return response


@router.get("/login/callback")
def callback(code: str, state: str):
    url = os.getenv("NAVER_OAUTH_TOKEN_URL")
    params = {
        "grant_type": "authorization_code",
        "client_id": os.getenv("NAVER_OAUTH_CLIENT_ID"),
        "client_secret": os.getenv("NAVER_OAUTH_CLIENT_SECRET"),
        "code": code,
        "state": state,
    }
    response = requests.get(url, params=params)
    return response.json()
