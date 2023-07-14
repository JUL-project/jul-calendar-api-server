import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("NAVER_OAUTH_LOGIN_URL")
ID = os.getenv("NAVER_OAUTH_CLIENT_ID")
KEY = os.getenv("NAVER_OAUTH_CLIENT_SECRET")
CALLBACK_URL = os.getenv("NAVER_OAUTH_CALLBACK_URL")

REQUEST_URL = "{}?response_type=code&client_id={}&redirect_uri={}&state".format(URL, ID, CALLBACK_URL)


def login():
    return REQUEST_URL
