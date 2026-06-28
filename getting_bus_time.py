import asyncio
import httpx
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("URL")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
async def getting_bus_time():
     try:
          async with httpx.AsyncClient(headers=HEADERS) as client:
               response = await client.get(url)
               soup = BeautifulSoup(response.text, "html.parser")
               time = soup.find("span", class_="masstransit-prognoses-view__title-text")
               chance = soup.find("div", class_="pulse-view _size_small _color_green")
               next_time = soup.find("div", class_="masstransit-prognoses-view__time")
               if time and next_time and chance:
                   return time.text, next_time.text, True
               elif time and next_time:
                    return time.text, next_time.text, False
               else:
                    return None, None , False
     except httpx.ConnectError:
           print("Не удалось подключиться к серверу (проблемы с DNS или сетью)")
           return None ,None , False
     except httpx.TimeoutException:
           print("Превышено время ожидания ответа")
           return None,None, False
     except httpx.HTTPStatusError as exc:
           print(f"Ошибка HTTP: {exc.response.status_code} для URL {exc.request.url}")
           return None,None, False
     except httpx.RequestError as exc:
           print(f"Произошла ошибка при отправке запроса: {exc}")
           return None,None, False