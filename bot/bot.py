import asyncio
import handlers
from config import *
from aiogram  import Bot, Dispatcher

async def main():
	bot = Bot(TOKEN)
	dp = Dispatcher()
	dp.include_routers(
		handlers.router,
	)
	await dp.start_polling(bot)

if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print("EXIT")