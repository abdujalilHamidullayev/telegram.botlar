from telegram import Update
from telegram.ext import  CallbackContext
from gtts import gTTS

def start(update,context):
    user=update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Salom @{user.username} bizning telegram botimizga hush kelibsiz")

def help(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text=f"salom mendan yordam soraizmi")

def exo(update: Update, context=CallbackContext):
    update.message.reply_text(update.message.text)

def text_to_audio(matn):
    speach=gTTS(text=matn)
    speach.save('audios/mars_17_30_mp3.')
    audio=open('audios/mars_17_30_mp3','rb')
    return audio
def xabar(update,context):
    message=update.message.text
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=text_to_audio(message))