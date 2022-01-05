from telegram import InlineKeyboardMarkup, InlineKeyboardButton
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="salom raspisaniya botiga hush kelibsiz")
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Dushanba", callback_data=1),
         InlineKeyboardButton("Seshanba", callback_data=2)],
         [
             InlineKeyboardButton("chorshanba", callback_data=3),
         InlineKeyboardButton("payshanba", callback_data=4)
         ],
         [
             InlineKeyboardButton("juma", callback_data=5),
         InlineKeyboardButton("shanba", callback_data='shanba')]
         ]

    )

    update.message.reply_text("Marhamat. Hafta kunini tanlang", reply_markup=reply_markup)







def dushanba(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Cherchenie\nUzbekskiy yazik\nAlgebra\nIstoriya\nRusskiy yazik\nAngliyskiy yazik")

def seshanba(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Algebra\nTexnologiya\nXimiya\nInformatika\nAngliski yazik\nVospitaniya")

def chorshanba(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Russki yazik\nUzbekski\nGeografiya\nGeometriya\nIstoria\nAngliski")

def payshanba(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ximiya\nBiologoya\nGeometriya\nFizra\nLiteratura\nFizika")

def juma(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text="Klassni chas\nXimiya\nUzbekski\nFizra\nLiteratura\nAlgebra")

def shanba(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                                                 text="Geografiya\nInformatika\nFizika\nGos prava\nIstoria\nEkonomika")

def kunlar(update,context):
    query=update.callback_query
    if query.data=="1":
        dushanba(update,context)
    elif query.data=='2':
        seshanba(update,context)
    elif query.data=="3":
        chorshanba(update, context)
    elif query.data == "4":
        payshanba(update, context)
    elif query.data == "5":
        juma(update, context)
    else:
        shanba(update,context)