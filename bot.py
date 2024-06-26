import logging
import os
import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define your bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')
PORT = int(os.environ.get('PORT', 8443))

# Database setup
conn = sqlite3.connect('bot.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    username TEXT,
    message TEXT
)
''')

conn.commit()

# Define command handlers
async def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hello! I am your Telegram bot.')

async def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message and log it."""
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    message = update.message.text

    cursor.execute('INSERT INTO messages (user_id, username, message) VALUES (?, ?, ?)',
                   (user_id, username, message))
    conn.commit()

    await update.message.reply_text(message)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=8444,
        url_path=BOT_TOKEN,
        webhook_url=f"https://tgpython01.onrender.com/{BOT_TOKEN}"
    )

if __name__ == '__main__':
    main()
