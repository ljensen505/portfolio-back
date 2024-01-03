import os

from dotenv import load_dotenv

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8000",
    "https://localhost:8000",
    "http://localhost:3000",
    "https://localhost:3000",
]


def get_token() -> str:
    import http.client
    import json

    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    conn = http.client.HTTPSConnection("lucasjensen.us.auth0.com")

    payload = (
        '{"client_id":"'
        + f"{client_id}"
        + '","client_secret":"'
        + f"{client_secret}"
        + '","audience":"'
        + f"https://api.lucasjensen.me/"
        + '","grant_type":"client_credentials"}'
    )

    headers = {"content-type": "application/json"}

    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()

    data = res.read()
    body = json.loads(data.decode("utf-8"))

    return body["access_token"]
