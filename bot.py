from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '6746078978:AAHjRhgeUWMXbHaZPmjGn_2I_wtYu_-Qhu8'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle /start command
def start(update: Update, context):
    update.message.reply_text('Hello! I am your bot.')

# Function to handle /help command
def help_command(update: Update, context):
    update.message.reply_text('Help command received.')

# Function to handle specific messages
def echo(update: Update, context):
    if update.message.text.lower() == 'hi':
        update.message.reply_text('Hello there!')
    elif update.message.text.lower() == 'how are you?':
        update.message.reply_text('I am fine, thank you!')
    else:
        update.message.reply_text('I did not understand your message.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handlers for commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Handler for messages
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

    # Start the Bot
    updater.start_polling()
    logger.info("Bot started polling...")

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
