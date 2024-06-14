from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configuración inicial
TOKEN = '7337308320:AAHltD0AhkXTQKC1B4QVkyL9PhHVBix9Epg'
WEB_APP_URL = 'https://tuservidor.com/car_game.html'  # Cambia esto por la URL donde alojarás tu archivo HTML

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Start Game", web_app=WEB_APP_URL),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Click to start the game', reply_markup=reply_markup)

def main() -> None:
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
