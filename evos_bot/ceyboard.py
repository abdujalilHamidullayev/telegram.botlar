from telegram.ext import ReplyKeyboardMarkup
from telegram.ext import InlineKeyboardMarkup, InlineKeyboardButton
from connect import get_menu1

asosiy_menu=ReplyKeyboardMarkup([
    ["🍽 Menu"],
    ["🖊Fikir bildirish","🛒Mening buyurtmam"]
], resiz_keybord=True)

category=get_menu1()
# print(category)

menu_1=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(category[0][1], callback_data=category[0][0]),
            InlineKeyboardButton(category[1][1], callback_data=category[1][0])
        ],
        [
            InlineKeyboardButton(category[2][1], callback_data=category[2][0]),
            InlineKeyboardButton(category[3][1], callback_data=category[3][0])
        ]
    ]
)