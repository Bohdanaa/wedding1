from flask import Flask, render_template, request
import telegram

app = Flask(__name__)

# Конфігурація Telegram Bot
BOT_TOKEN = "6139494128:AAFF81pUP18MzObbGas48aBnlQnxn_9C42U"
CHAT_ID  = "500842187"
bot = telegram.Bot(token=BOT_TOKEN)

# Основна сторінка з формою
@app.route('/')
def index():
    return render_template('index.html')

# Обробка відправленої форми
@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    choice = request.form['choice']
    drinks = request.form['drinks']

    # Відправка повідомлення на Telegram
    bot.send_message(chat_id=CHAT_ID, text=f'Нове повідомлення:\nІм\'я: {name}\nЕлектронна пошта: {choice}\nПовідомлення: {drinks}')

    return 'OK'

if __name__ == '__main__':
    app.run()
