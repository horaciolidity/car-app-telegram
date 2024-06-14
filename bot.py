from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
import logging

# Configuración inicial
TOKEN = '7337308320:AAHltD0AhkXTQKC1B4QVkyL9PhHVBix9Epg'
WEB_APP_URL = 'https://car-app-telegram.vercel.app/'  # URL de tu Web App

# Configuración de logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Start Game", web_app=WebAppInfo(url=WEB_APP_URL)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Click to start the game', reply_markup=reply_markup)

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
