from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram_bot_pagination import InlineKeyboardPaginator
from get_db import (
    get_db,
    get_photo
)
from telebot import TeleBot
from decouple import config


bot = TeleBot(config('TOKEN'))


def characters_page_callback(call):
    calli = call.data
    if calli == 'back':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    else:
        page = int(calli.split('#')[1])
        bot.delete_message(
            call.message.chat.id,
            call.message.message_id
        )
        send_character_page(call.message, page)


def send_character_page(message, page=1):
    try:
        chat_id = message.chat.id
    except:
        chat_id = message.message.chat.id
    db = get_db('Saosyant-Desatir_text')
    paginator = InlineKeyboardPaginator(
        len(db),
        current_page=page,
        data_pattern='character#{page}'
    )
    paginator.add_after(InlineKeyboardButton('В главное меню', callback_data='menu'))
    photo = get_db('download_photo')[page-1]['photo_download']
    if db[page-1] != 'photo':
        bot.send_photo(
            chat_id,
            photo=photo,
            caption=db[page-1],
            reply_markup=paginator.markup,
            parse_mode='Markdown',
            timeout=60
        )
    else:
        bot.send_photo(
            message.chat.id,
            photo=photo,
            reply_markup=paginator.markup,
            parse_mode='Markdown',
            timeout=60
        )


def atman(message):
    chat_id = message.message.chat.id
    db = get_db('throne')
    for i in db:
        if i['name'] == 'Atman':
            obj = i['desc'] 
            photo = get_photo('Atman')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def remorseless(message):
    chat_id = message.message.chat.id
    db = get_db('throne')
    for i in db:
        if i['name'] == 'Remorseless':
            obj = i['desc']
            photo = get_photo('Remorseless')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def morningstar(message):
    chat_id = message.message.chat.id
    db = get_db('throne')
    for i in db:
        if i['name'] == 'Morningstar':
            obj = i['desc']
            photo = get_photo('Morningstar')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def mercurius(message):
    chat_id = message.message.chat.id
    db = get_db('throne')
    for i in db:
        if i['name'] == 'Mercurius':
            obj = i['desc']   
            photo = get_photo('Mercurius')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def mephistopheles(message):
    chat_id = message.message.chat.id
    db = get_db('throne')
    for i in db:
        if i['name'] == 'Mephistopheles':
            obj = i['desc'] 
            photo = get_photo('Gold')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def zarathustra(message):
    chat_id = message.message.chat.id
    db = get_db('throne')
    for i in db:
        if i['name'] == 'Zarathustra':
            obj = i['desc']  
            photo = get_photo('Ren')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def twilight(message):
    chat_id = message.message.chat.id
    db = get_db('throne')
    for i in db:
        if i['name'] == 'Twilight':
            obj = i['desc'] 
            photo = get_photo('Mari')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def hajun(message):
    chat_id = message.message.chat.id
    db = get_db('throne')
    for i in db:
        if i['name'] == 'Hajun':
            obj = i['desc']   
            photo = get_photo('Hajun')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def amaterasu(message):
    chat_id = message.message.chat.id
    db = get_db('throne')
    for i in db:
        if i['name'] == 'Amaterasu':
            obj = i['desc']     
            photo = get_photo('Amaterasu')
            keyboard = InlineKeyboardMarkup(row_width=1)
            btn1 = InlineKeyboardButton('Назад', callback_data='Back')
            keyboard.add(btn1)
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown", reply_markup=keyboard)


def dies_gods(message): 
    chat_id = message.message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Истина', callback_data='Atman')
    btn2 = InlineKeyboardButton('Бессердечность', callback_data='Remorseless')
    btn3 = InlineKeyboardButton('Утренняя Звезда', callback_data='Morningstar')
    btn4 = InlineKeyboardButton('Ртуть', callback_data='Mercurius')
    btn5 = InlineKeyboardButton('Сумерки', callback_data='Twilight')
    btn6 = InlineKeyboardButton('Хадзюн', callback_data='Hajun')
    btn7 = InlineKeyboardButton('Рассвет', callback_data='Amaterasu')
    btn8 = InlineKeyboardButton('Мгновение', callback_data='Zarathustra')
    btn9 = InlineKeyboardButton('Золото', callback_data='Mephistopheles')
    btn10 = InlineKeyboardButton('В главное меню', callback_data='menu')
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    bot.send_message(chat_id, 'Боги Престола', reply_markup=keyboard)


def gods_btn(commands):
    if commands.data == 'Divine':
        dies_gods(commands)
    elif commands.data == 'Atman':
        atman(commands)                                                               
    elif commands.data == 'Remorseless':
        remorseless(commands)
    elif commands.data == 'Morningstar':
        morningstar(commands)
    elif commands.data == 'Mercurius':
        mercurius(commands)
    elif commands.data == 'Twilight':
        twilight(commands)
    elif commands.data == 'Hajun':
        hajun(commands)
    elif commands.data == 'Amaterasu':
        amaterasu(commands)
    elif commands.data == 'Zarathustra':
        zarathustra(commands)
    elif commands.data == 'Mephistopheles':
        mephistopheles(commands)
    elif commands.data == 'Back':
        dies_gods(commands)
    
def saosyant_btn(commands):
    try:
        if commands.data.split('#')[0] in 'character':
            page = int(commands.data.split('#')[1])
            send_character_page(commands.message, page)
    except:
        None