from telegram.ext import Updater,ConversationHandler, Filters
from telegram.ext import CommandHandler, MessageHandler
from methods import start,get_tel

updater=Updater(token='5018569131:AAEqhjqhjltlmMBx26mOY2xF6f_2vXWw1EU',use_context=True)
dispatcher=updater.dispatcher
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start',start)],
    states={
        1:[MessageHandler(Filters.text,get_tel)]


    }
    falbacks=[MessangeHandler(Filters.text, start)]
)

dispatcher.add_handler(conv_handler)



updater.start_polling()
print("hammasi yahshi, yangi yil bilan")



