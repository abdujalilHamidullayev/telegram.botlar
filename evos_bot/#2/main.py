def start(update, context)
    user=update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id,text="Salom @{user.username}. Universal_botga hush kelibsiz!")
