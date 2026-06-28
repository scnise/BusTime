from aiogram import Router 
from aiogram.types import Message
from aiogram.filters import CommandStart
from timenow import now
#from adding_user import adding_user
router = Router()
@router.message(CommandStart())   
async def start(message: Message):
     await message.answer("Добро пожаловать в бота!")
     username = message.from_user.username or message.from_user.first_name
     userid= message.from_user.id
     timenow = now()
     # await adding_user(userid, username, timenow)