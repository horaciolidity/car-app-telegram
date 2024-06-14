import json
import requests
from flask import Flask, request

# Configuración inicial
TOKEN = '7337308320:AAHltD0AhkXTQKC1B4QVkyL9PhHVBix9Epg'
WEB_APP_URL = 'https://car-app-telegram.vercel.app/'  # URL de tu Web App

app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        message_id = data['message']['message_id']
        text = data['message'].get('text', '')

        if text == '/start':
            keyboard = {
                'inline_keyboard': [
                    [{'text': 'Start Game', 'url': WEB_APP_URL}]
                ]
            }
            reply_markup = json.dumps(keyboard)
            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
            requests.post(url, json={'chat_id': chat_id, 'text': 'Click to start the game', 'reply_markup': reply_markup})

    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
