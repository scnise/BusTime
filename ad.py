import asyncio
import qrcode
from aiogram import Bot, Dispatcher, F
from aiogram.types import FSInputFile, Message
from aiogram.filters import Command, CommandStart
import os
token = os.getenv("TOKEN")
db = Dispatcher()
bot = Bot(token)
async def main():
    await db.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())