import asyncio
import aiosqlite
from aiogram import Bot, Dispatcher,F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from dotenv import load_dotenv
import os
from datetime import datetime
import httpx
from bs4 import BeautifulSoup
load_dotenv()
Token = os.getenv("TOKEN")
url = os.getenv("URL")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
bot = Bot(token=Token)
dp = Dispatcher()
@dp.message(CommandStart())   
async def start(message: Message):
     await message.answer("Добро пожаловать в бота!")
     ##message приветствия и добавление человека в бд
     username = message.from_user.username or message.from_user.first_name
     userid= message.from_user.id
     timenow = now()
     await adding_user(userid, username, timenow)
@dp.message(F.text)
async def messages(message: Message):
     if message.text.lower() == "автобус":
          timebus , nexttimebus = await getting_bus_time()
          ostanovka = "w"
          await message.answer(f"Следующий автобус на {ostanovka} будет через {timebus},потом {nexttimebus}")
async def find_user(a):
    async with aiosqlite.connect("bot_data.db") as db:
        cursor = await db.execute("SELECT * FROM users WHERE userid = ?;",(a,))
        res = await cursor.fetchone()
        if res:
            return res
        else:
            return None
async def main():
     await bot.delete_webhook(drop_pending_updates=True)
     await dp.start_polling(bot)
async def getting_bus_time():
     try:
          async with httpx.AsyncClient(headers=HEADERS) as client:
               response = await client.get(url)
               soup = BeautifulSoup(response.text, "html.parser")
               time = soup.find("span", class_="masstransit-prognoses-view__title-text")
               next_time = soup.find("div", class_="masstransit-prognoses-view__time")
               if time and next_time:
                   return time.text, next_time.text
               else:
                    return None, None
     except httpx.ConnectError:
           print("Не удалось подключиться к серверу (проблемы с DNS или сетью)")
           return None ,None
     except httpx.TimeoutException:
           print("Превышено время ожидания ответа")
           return None,None
     except httpx.HTTPStatusError as exc:
           print(f"Ошибка HTTP: {exc.response.status_code} для URL {exc.request.url}")
           return None,None
     except httpx.RequestError as exc:
           print(f"Произошла ошибка при отправке запроса: {exc}")
           return None,None
def now():
    now = datetime.now()
    time_date = now.strftime("%H:%M:%S %d.%m.%Y")
    return time_date
async def adding_user(a,b,c):
     async with aiosqlite.connect("bot_data.db") as db:
          cursor = await db.execute("SELECT * FROM users WHERE userid = ?;",(a,))
          res = await cursor.fetchone()
          if not res:
               await db.execute("INSERT INTO users (userid, username, start_time) VALUES (? , ?, ?);", (a,b,c))
               await db.commit()
if __name__ == "__main__":
    asyncio.run(main())