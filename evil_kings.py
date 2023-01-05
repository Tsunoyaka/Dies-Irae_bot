from telebot import TeleBot
from telebot.types import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton
    )
from get_db import (
    get_db,
    get_photo_evil_kings,
)
from decouple import config


bot = TeleBot(config('TOKEN'))


def evil_kings(message): 
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Фарн', callback_data='Khvarenah')
    btn2 = InlineKeyboardButton('Бахраван', callback_data='Bahlavan')
    btn3 = InlineKeyboardButton('Надаре', callback_data='Nadare')
    btn4 = InlineKeyboardButton('Фредерика', callback_data='Frederica')
    btn5 = InlineKeyboardButton('Машъяна', callback_data='Mashyana')
    btn6 = InlineKeyboardButton('Кайхосру', callback_data='Kaikhosru')
    btn7 = InlineKeyboardButton('Ака Мана', callback_data='Aka-Manah')
    btn8 = InlineKeyboardButton('Назад', callback_data='Back_First_Heaven')
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(chat_id, 'Короли Зла', reply_markup=keyboard)


def dragvant(message): 
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Монсеррат', callback_data='Munsarat')
    btn2 = InlineKeyboardButton('Таурвид', callback_data='Taurvid')
    btn3 = InlineKeyboardButton('Заиричед', callback_data='Zariched')
    btn4 = InlineKeyboardButton('Роксанна', callback_data='Roxanni')
    btn5 = InlineKeyboardButton('Назад', callback_data='Back_First_Heaven')
    keyboard.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(chat_id, 'Друджванты', reply_markup=keyboard)


def super_evil_kings(commands):
    chat_id = commands.message.chat.id
    db = get_db('Evil_Kings')
    for i in db:
        if i['name'] == commands.data:
            obj = i['desc']     
            photo = get_photo_evil_kings(commands.data)
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back_Evil')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def super_daeva(commands):
    chat_id = commands.message.chat.id
    db = get_db('Dragvant')
    for i in db:
        if i['name'] == commands.data:
            obj = i['desc']     
            photo = get_photo_evil_kings(commands.data)
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back_Daeva')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def evil_kings_btn(commands):
    if commands.data == 'Back_Evil':
        evil_kings(commands.message)
    elif commands.data == 'Evil_Kings':
        evil_kings(commands.message)
    elif commands.data == 'Dragvant':
        dragvant(commands.message)
    elif commands.data == 'Back_Daeva':
        dragvant(commands.message)
    elif commands.data in ['Khvarenah', 'Bahlavan', 'Nadare', 
    'Frederica', 'Mashyana', 'Kaikhosru','Aka-Manah']:
        super_evil_kings(commands)
    elif commands.data in ['Munsarat', 'Roxanni', 'Taurvid', 'Zariched']:
        super_daeva(commands)