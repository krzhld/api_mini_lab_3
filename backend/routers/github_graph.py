import urllib
from urllib.request import urlopen
import json
import requests
from fastapi import APIRouter
from backend.config import settings
from PIL import Image

github_router = APIRouter(prefix='/github', tags=['Github'])


@github_router.get("/{username}/the_last_follower")
async def root(username: str = "krzhld"):
    token = settings.GITHUB_API_TOKEN
    headers = {
      "authorization": f"token {token}"
    } if token else {}

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=headers)
    user_data = response.json()
    followers_url = user_data["followers_url"]
    json_url = urlopen(followers_url)
    followers_data = json.loads(json_url.read())
    last_follower = followers_data[-1]

    if response.status_code == 200:  # Проверка кода ответа
        return last_follower
    elif response.status_code == 401:
        return {"status": 401,
                "message": "Invalid authorization token"}  # Отправляем своё сообщение и код ошибки
    elif response.status_code == 404:
        return {"status": 404, "message": "Not found"}


@github_router.get("/{username}/size")
async def root(username: str = "krzhld"):
    token = settings.GITHUB_API_TOKEN
    headers = {
      "authorization": f"token {token}"
    } if token else {}

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=headers)
    user_data = response.json()
    avatar_url = user_data["avatar_url"]

    image = Image.open(urllib.request.urlopen(avatar_url))
    width, height = image.size

    if response.status_code == 200:  # Проверка кода ответа
        return {"width": width, "height": height}
    elif response.status_code == 401:
        return {"status": 401,
                "message": "Invalid authorization token"}  # Отправляем своё сообщение и код ошибки
    elif response.status_code == 404:
        return {"status": 404, "message": "Not found"}


@github_router.get("/{username}/followers")
async def root(username: str = "krzhld"):
    token = settings.GITHUB_API_TOKEN
    headers = {
      "authorization": f"token {token}"
    } if token else {}

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=headers)
    user_data = response.json()
    followers_url = user_data['followers_url']
    json_url = urlopen(followers_url)
    followers_data = json.loads(json_url.read())

    if response.status_code == 200:  # Проверка кода ответа
        return followers_data
    elif response.status_code == 401:
        return {"status": 401, "message": "Invalid authorization token"}  # Отправляем своё сообщение и код ошибки
    elif response.status_code == 404:
        return {"status": 404, "message": "Not found"}


@github_router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello, {name}!"}


@github_router.get("/{username}/name")
async def root(username: str = "krzhld"):
    token = settings.GITHUB_API_TOKEN
    headers = {
      "authorization": f"token {token}"
    } if token else {}

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=headers)
    user_data = response.json()
    name = user_data['name']

    if response.status_code == 200:  # Проверка кода ответа
        return {"name": name}
    elif response.status_code == 401:
        return {"status": 401, "message": "Invalid authorization token"}  # Отправляем своё сообщение и код ошибки
    elif response.status_code == 404:
        return {"status": 404, "message": "Not found"}
