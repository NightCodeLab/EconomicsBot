from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(
	inline_keyboard=[
		[InlineKeyboardButton(text="Мои разработчики", url="https://t.me/nightcodelab")],
		[InlineKeyboardButton(text="Мой исходный код🌐", url="https://github.com/NightCodeLab/EconomicsBot")]
	]
)