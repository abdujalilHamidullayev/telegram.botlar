from telegram.ext import Updater, ConversationHandler, Filters
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler
from method import start, get_number, get_menu, get_fikr, atvet_fikr, button
from method import lavashlar, burgerlar, shourmalar, ichimliklar
from keybord import asosiy_menu

updater=Updater(token='5073225373:AAFzu1R0ygfGlN6uYM8llz64zmpuUqq82lE',use_context=True)
dispatcher=updater.dispatcher

conv_hundler=ConversationHandler(
    entry_points=[CommandHandler('start',start)],
    states={
        1:[MessageHandler(Filters.text,get_number)],
        2:[
            MessageHandler(Filters.regex("🍽 Menu"), get_menu),
            MessageHandler(Filters.regex("🖊Fikir bildirish"),get_fikr),
            # MessageHandler(Filters.regax("🛒Mening buyurtmam"))
            ],
        3:[MessageHandler(Filters.text,atvet_fikr)],
        4:[
            MessageHandler(Filters.regex("Lavashlar"), lavashlar),
            MessageHandler(Filters.regex("Burgerlar"), burgerlar),
            MessageHandler(Filters.regex("Shourmalar"), shourmalar),
            MessageHandler(Filters.regex("Ichimliklar"), ichimliklar()),
        ]
        # 4:[CallbackQueryHandler(button)],
    },
    fallbacks=[MessageHandler(Filters.text, start)]
)

dispatcher.add_handler(conv_hundler)
updater.start_polling()
print("Barchsi yahshi")