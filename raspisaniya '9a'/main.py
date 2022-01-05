from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from methods import start, kunlar

updater = Updater(token="5032376512:AAEzM9GlCcehCMjiqMLkSX6evXTKBPE44ek")

dispatcher = updater.dispatcher

start_handler = CommandHandler("start", start)

message_handler=CallbackQueryHandler(kunlar)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()


print("ok hammasi yahshi")