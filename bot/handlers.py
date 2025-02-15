import requests
import config
import keyboards
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery


router = Router()


@router.message(CommandStart())
async def start(message: Message):
	await message.answer(config.start_msg, parse_mode="MarkDown", reply_markup=keyboards.start_kb)


@router.message(Command("incomes"))
async def incomes(message: Message):
	response = requests.get(url=f"{config.API_URL}{message.from_user.id}/incomes").json()
	total_amount = sum(item['amount'] for item in response)
	answer = "\n\n".join(
		[f"🆔ID: {item['id']}\n💸Сумма: {item['amount']}\n📆Дата: {item['date']}\n📑Описание: {item['description']}" for item in response]
	)
	await message.answer(f"Прибыль / +{total_amount}\n{answer}")


@router.message(Command("spends"))
async def incomes(message: Message):
	response = requests.get(url=f"{config.API_URL}{message.from_user.id}/spends").json()
	total_amount = sum(item['amount'] for item in response)
	answer = "\n\n".join(
		[f"🆔ID: {item['id']}\n💸Сумма: {item['amount']}\n📆Дата: {item['date']}\n📑Описание: {item['description']}" for item in response]
	)
	await message.answer(f"Расходы / -{total_amount}\n{answer}")


@router.message()
async def ed(message: Message):
	message_command = message.text.split(" ", 2)
	try:
		ent = message_command[0]
		summ = message_command[1]
		description = message_command[2]
		if ent == "+":
			response = requests.get(url=f"{config.API_URL}income/{message.from_user.id}/{summ}/{description}")
			await message.answer(f"Прибыль: {summ}\nОписание: {description}")

		elif ent == "-":
			response = requests.get(url=f"{config.API_URL}spending/{message.from_user.id}/{summ}/{description}")
			await message.answer(f"Потрачено: {summ}\nОписание: {description}")

	except IndexError as index:
		if ent == "+":
			response = requests.get(url=f"{config.API_URL}income/{message.from_user.id}/{summ}/Без описания")
			await message.answer(f"Прибыль: {summ}\nОписание: {description}")

		elif ent == "-":
			response = requests.get(url=f"{config.API_URL}spending/{message.from_user.id}/{summ}/Без описания")
			await message.answer(f"Потрачено: {summ}\nОписание: {description}")
