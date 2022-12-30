import telebot
from telebot.types import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton
    )
from get_db import (
    get_db,
    get_photo_evil_kings,
)
from decouple import config


bot = telebot.TeleBot(config('TOKEN'))


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
    btn8 = InlineKeyboardButton('В главное меню', callback_data='menu')
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(chat_id, 'Короли Зла', reply_markup=keyboard)


def khvarenah(message):
    chat_id = message.chat.id
    db = get_db('Evil_Kings')
    for i in db:
        if i['name'] == 'Khvarenah':
            obj = i['desc']     
            photo = get_photo_evil_kings('Khvarenah')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back_Evil')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def bahlavan(message):
    chat_id = message.chat.id
    db = get_db('Evil_Kings')
    for i in db:
        if i['name'] == 'Bahlavan':
            obj = i['desc']     
            photo = get_photo_evil_kings('Bahlavan')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back_Evil')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def nadare(message):
    chat_id = message.chat.id
    db = get_db('Evil_Kings')
    for i in db:
        if i['name'] == 'Nadare':
            obj = i['desc']     
            photo = get_photo_evil_kings('Nadare')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back_Evil')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def frecerica(message):
    chat_id = message.chat.id
    db = get_db('Evil_Kings')
    for i in db:
        if i['name'] == 'Frederica':
            obj = i['desc']     
            photo = get_photo_evil_kings('Frederica')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back_Evil')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def mashyana(message):
    chat_id = message.chat.id
    db = get_db('Evil_Kings')
    for i in db:
        if i['name'] == 'Mashyana':
            obj = i['desc']     
            photo = get_photo_evil_kings('Mashyana')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back_Evil')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def kaikhosru(message):
    chat_id = message.chat.id
    db = get_db('Evil_Kings')
    for i in db:
        if i['name'] == 'Kaikhosru':
            obj = i['desc']     
            photo = get_photo_evil_kings('Kaikhosru')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back_Evil')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def aka_manah(message):
    chat_id = message.chat.id
    db = get_db('Evil_Kings')
    for i in db:
        if i['name'] == 'Aka_Manah':
            obj = i['desc']     
            photo = get_photo_evil_kings('Aka-Manah')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back_Evil')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def evil_kings_btn(commands):
    if commands.data == 'Back_Evil':
        evil_kings(commands.message)
    if commands.data == 'Evil_Kings':
        evil_kings(commands.message)
    if commands.data == 'Khvarenah':
        khvarenah(commands.message)
    if commands.data == 'Bahlavan':
        bahlavan(commands.message)
    if commands.data == 'Nadare':
        nadare(commands.message)
    if commands.data == 'Frederica':
        frecerica(commands.message)
    if commands.data == 'Mashyana':
        mashyana(commands.message)
    if commands.data == 'Kaikhosru':
        kaikhosru(commands.message)
    if commands.data == 'Aka-Manah':
        aka_manah(commands.message)
