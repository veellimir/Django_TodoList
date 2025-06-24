import httpx

from settings.env_config import ENV__API_BACKEND


async def get_tasks(telegram_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{ENV__API_BACKEND}tasks/", params={"telegram_id": telegram_id}
        )
        return response.json()


async def add_task(telegram_id: int, title: str, category_id: str, due_date: str):
    async with httpx.AsyncClient() as client:
        payload = {
            "title": title,
            "description": "",
            "due_date": due_date,
            "user": telegram_id,
            "category": category_id,
        }
        response = await client.post(
            f"{ENV__API_BACKEND}tasks/", json=payload
        )
        return response.status_code == 201
