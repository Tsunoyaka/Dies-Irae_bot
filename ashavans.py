from telebot import TeleBot
from telebot.types import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton
    )
from decouple import config

from get_db import (
    get_db,
    get_photo_yazata
)

bot = TeleBot(config('TOKEN'))

def ashavans(message): 
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton('Cвириос', callback_data='Sirius')
    btn2 = InlineKeyboardButton('Вархран', callback_data='Varhram')
    btn3 = InlineKeyboardButton('Нахид', callback_data='Nahid')
    btn4 = InlineKeyboardButton('Ахурамазда', callback_data='Ahura_Mazda')
    btn5 = InlineKeyboardButton('Магсарион', callback_data='Magsarion')
    btn6 = InlineKeyboardButton('Квинн', callback_data='Quinn')
    btn7 = InlineKeyboardButton('Зурван', callback_data='Zurvan')
    btn8 = InlineKeyboardButton('Фердоус', callback_data='Ferdowsi')
    btn9 = InlineKeyboardButton('Самлук', callback_data='Samluch')
    btn10 = InlineKeyboardButton('Арма', callback_data='Alma')
    btn11 = InlineKeyboardButton('Ашозушта', callback_data='Ashozushta')
    btn12 = InlineKeyboardButton('Инцест', callback_data='Insesuto')
    btn13 = InlineKeyboardButton('Роксанна', callback_data='Roxanne')
    btn14 = InlineKeyboardButton('Назад', callback_data='Back_First_Heaven')
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
    keyboard.add(btn14)
    bot.send_message(chat_id, 'Ашаваны', reply_markup=keyboard)


def super_ashavans(commands):
    chat_id = commands.message.chat.id
    db = get_db('Yazata')
    for i in db:
        if i['name'] == commands.data:
            obj = i['desc']     
            photo = get_photo_yazata(commands.data)
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back_Ashavans')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def ashavans_btn(commands):
    if commands.data == 'Back_Ashavans':
        ashavans(commands.message)
    elif commands.data == 'Ashavans':
        ashavans(commands.message)
    elif commands.data in ['Sirius', 'Varhram', 'Nadare', 'Nahid', 'Magsarion', 'Quinn', 'Zurvan',
    'Ferdowsi', 'Samluch', 'Alma', 'Ashozushta', 'Roxanne', 'Insesuto', 'Ahura_Mazda']:
        super_ashavans(commands)