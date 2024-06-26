import asyncio
from aiogram import Bot, Dispatcher, types

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
    # Start long-polling
    await dp.start_polling()

    # Run the bot until it receives SIGINT, SIGTERM or SIGABRT
    await dp.idle()

if __name__ == '__main__':
    # Create event loop
    loop = asyncio.get_event_loop()
    # Run main coroutine
    loop.run_until_complete(main())
