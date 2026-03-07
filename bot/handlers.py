from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from database import get_user, create_user
from agent_bridge import answer_agent


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Я бюджет бот.")

@router.message()
async def echo(message: Message):
    user_id = message.from_user.id
    user_message = message.text

    if get_user(user_id) is None:
        create_user(user_id)

    response = answer_agent(user_id, user_message)
    await message.answer(response)

