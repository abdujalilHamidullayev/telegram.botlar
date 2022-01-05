from telegram.ext import Updater,  CommandHandler,Filters
from telegram.ext import MessageHandler
from metods import start, xabar, exo



updater=Updater(token="5018569131:AAEqhjqhjltlmMBx26mOY2xF6f_2vXWw1EU", use_context=True)
dispatcher=updater.dispatcher

start_handler=CommandHandler('start',start)
message_handler=MessageHandler(Filters.text,xabar)
help_handler=CommandHandler('help',help)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
# dispatcher.add_handler(MessageHandler(Filters.text,exo))
dispatcher.add_handler(message_handler)



updater.start_polling()
print("ok,bot yaxshi ishlayapti")


