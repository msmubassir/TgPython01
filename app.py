import os  # Add this line at the top
from flask import Flask, request, render_template
from telegram import Bot
import sqlite3

app = Flask(__name__)
bot = Bot(token=os.getenv('BOT_TOKEN'))

# Database setup
conn = sqlite3.connect('bot.db', check_same_thread=False)
cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute('SELECT * FROM messages')
    messages = cursor.fetchall()
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    user_id = request.form['user_id']
    message = request.form['message']
    bot.send_message(chat_id=user_id, text=message)
    return 'Message sent!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
