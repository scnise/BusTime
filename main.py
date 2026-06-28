import asyncio
from aiogram import Bot, Dispatcher,F
from dotenv import load_dotenv
import os
from start import router as start
from sendingbus import router as bus
load_dotenv()
Token = os.getenv("TOKEN")
bot = Bot(token=Token)
dp = Dispatcher()
async def main():
     dp.include_router(start)
     dp.include_router(bus)
     await bot.delete_webhook(drop_pending_updates=True)
     await dp.start_polling(bot)
     
if __name__ == "__main__":
    asyncio.run(main())
    
