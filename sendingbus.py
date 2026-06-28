from aiogram import Router , F
from aiogram.types import Message
from getting_bus_time import getting_bus_time
router = Router()
@router.message(F.text.lower() == "автобус")
async def messages(message: Message):
          timebus , nexttimebus , istrue  = await getting_bus_time()
          if not timebus or not nexttimebus:
            await message.answer("Извините, не удалось получить расписание автобусов. Попробуйте позже.")
            return
          ostanovka = "w"
          if istrue:
             await message.answer(f"Следующий автобус будет через {timebus}(100%),потом {nexttimebus}")
          else: 
             await message.answer(f"Следующий автобус будет через {timebus}(по расписанию),потом {nexttimebus}")