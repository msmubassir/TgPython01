from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function for /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am your bot.")

# Define a function for handling messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token='6746078978:AAHjRhgeUWMXbHaZPmjGn_2I_wtYu_-Qhu8', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handler for /start command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Register handler for messages
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
