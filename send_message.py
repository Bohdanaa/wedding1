import requests

from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


# Конфігурація параметрів для телеграм-бота
bot_token = "6139494128:AAFF81pUP18MzObbGas48aBnlQnxn_9C42U"
chat_id = "500842187"

# Отримання даних з форми
name = input("Ім'я: ")
choice = input("Чи будете брати участь?: ")
drinks = input("Оберіть алкогольний напій: ")

# Відправлення повідомлення в телеграм-бота
message = f"Ім'я: {name}\nЧи будете брати участь?: {choice}\nОбраний алкогольний напій: {drinks}"
telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {
    "chat_id": chat_id,
    "text": message
}
response = requests.post(telegram_api_url, json=payload)

if response.status_code == 200:
    print("Повідомлення надіслано успішно.")
else:
    print("Помилка при відправці повідомлення.")
if __name__ == '__main__':
    app.run()

