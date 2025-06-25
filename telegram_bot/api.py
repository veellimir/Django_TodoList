import httpx

from typing import List

from settings.env_config import ENV__API_BACKEND


async def get_tasks(telegram_id: int) -> List[dict]:
    try:
        async with httpx.AsyncClient() as client:
            url = f"{ENV__API_BACKEND}tasks/"
            response = await client.get(url, params={'telegram_id': str(telegram_id)})

        if response.status_code != 200:
            return []
        return response.json()
    except Exception:
        return []


async def add_task(title: str, description: str, due_date: str, username: str, category_name: str):
    try:
        async with httpx.AsyncClient() as client:
            url = f"{ENV__API_BACKEND}tasks/"
            payload = {
                'title': title,
                'description': description,
                'due_date': due_date,
                'username': username,
                'category_name': category_name,
            }
            response = await client.post(url, json=payload)
        return response.status_code == 201
    except Exception:
        return False


async def get_category_by_name(name: str) -> dict | None:
    try:
        async with httpx.AsyncClient() as client:
            url = f"{ENV__API_BACKEND}categories/"
            response = await client.get(url)
        if response.status_code != 200:
            return None
        categories = response.json()
        return next((c for c in categories if c['name'].lower() == name.lower()), None)
    except Exception:
        return None


async def get_user_by_username(username: str) -> dict | None:
    try:
        async with httpx.AsyncClient() as client:
            url = f"{ENV__API_BACKEND}users/{username}/"
            response = await client.get(url)
        if response.status_code != 200:
            return None
        return response.json()
    except Exception:
        return None
