from connect import  add_users
def start(update.context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Salom Evos Botga hush kelibsiz, mualif @abu_band1t")
    context.bot.send_message( chat_id=update.effective_chat.id,text="Marxamat ismingizni telefon raqamingizni kiriting:)
    return 1
def get_tel(update,context):
    matn=update.message.from_user.id
    user_id=update.message.from_user.id
    frist_name=update.message.from_user.first_name
    add_users(user_id,first_name,matn)

