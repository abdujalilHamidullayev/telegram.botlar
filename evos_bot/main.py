from connect import add_users
from ceyboard import asosiy_menu, menu_1
from connect import get_menu1

def start(update,context):
    user=update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Salom {user.first_name} men \"Evos\" fast food sentirining menusini chiqarib beraman")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Marxamat telefon raqamingizni kiriting")
    return 1

def get_number(update, context):
    matn=update.message.text
    user_id=update.message.from_user.id
    first_name=update.message.from_user.first_name
    add_users(user_id,first_name,matn)
    context.bot.send_message(chat_id=update.effextive_chat.id, text="Marxamat kerakli bo'limni tanlang", reply_markup=asosiy_menu)
    return 2

def get_menu(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Marhamat kerakli kategoriyani tanlang", reply_markup=menu_1)
    return 4

def button(update, context):
    query=update.callback_query
    for i in get_menu1():
        if i[0]==int(query.data):
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Siz \"{i[1]}\" categoriyasini tanladingiz")

def get_fikr(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Marxamat so'ylang, nima muammo?")
    return 3

def atvet_fikr(update, context):
    user=update.message.from_user
    shikoyat=update.message.text

    context.bot.send_message(chat_id=1050425024, text=f"Sizga yangi fikr keldi:\n")
    context.bot.send_message(chat_id=1050425024, text=f"\"{shikoyat}\"\nFikr muallifi: @{user.username}")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bo'ldi tamom, hal qilamiz!")