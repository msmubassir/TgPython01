import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '6746078978:AAHjRhgeUWMXbHaZPmjGn_2I_wtYu_-Qhu8'

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Handler for /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Hello! I am your bot.")

# Handler for /help command
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("Help command received.")

# Handler for specific messages
@dp.message_handler(lambda message: message.text.lower() == 'hi')
async def say_hi(message: types.Message):
    await message.answer("Hello there!")

@dp.message_handler(lambda message: message.text.lower() == 'how are you?')
async def say_how_are_you(message: types.Message):
    await message.answer("I am fine, thank you!")

# Main function to start the bot
async def main():
    # Start the long-polling mode
    await executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    # Run the main coroutine
    asyncio.run(main())
