import telebot
from telebot.types import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton
    )

from thron_gods import gods_btn, send_character_page, saosyant_btn
from evil_kings import evil_kings_btn
from get_db import (
    get_db,
    write_db,
    get_photo_yazata,
    get_id
)
from music import music_btn
from decouple import config


bot = telebot.TeleBot(config('TOKEN'))

@bot.message_handler(commands=['start'])
def welcome(message):
    dies_help(message)

@bot.message_handler(commands=['dies_help'])
def dies_help(message):
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Боги престола', callback_data='Divine')
    btn2 = InlineKeyboardButton('Короли Зла', callback_data='Evil_Kings')
    btn3 = InlineKeyboardButton('Pantheon: Saosyant Desatir', callback_data='Saosyant-Desatir')
    btn4 = InlineKeyboardButton('Музыка', callback_data='music')
    btn5 = InlineKeyboardButton('Перейти к источнику', url='https://vk.com/dies_irae_light')
    btn6 = InlineKeyboardButton('Скрыть', callback_data='skip')
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(chat_id, 'Выберите нужный вам список:', reply_markup=keyboard)


@bot.message_handler(commands=['Magsarion'])
def magsarion(message):
    chat_id = message.chat.id
    db = get_db('Yazata')
    for i in db:
        if i['name'] == 'Magsarion':
            obj = i['desc']     
            photo = get_photo_yazata('Magsarion')
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown")


@bot.message_handler(commands=['Ferdowsi'])
def ferdowsi(message):
    chat_id = message.chat.id
    db = get_db('Yazata')
    for i in db:
        if i['name'] == 'Ferdowsi':
            obj = i['desc']     
            photo = get_photo_yazata('Ferdowsi')
            bot.send_photo(chat_id, photo, caption=obj, parse_mode="Markdown")


def del_filter(commands):
    if not commands.data in ['del', 'Delete', 'one', 'two', 'three', 'four', 'five', 'mus_back', 
    'one_bey', 'two_bey', 'one_kajiri', 'two_kajiri', 'three_kajiri', 'four_kajiri']:
        bot.delete_message(commands.message.chat.id, commands.message.message_id)
    elif commands.data == 'Delete':
        bot.delete_message(commands.message.chat.id, commands.message.message_id)


def my_userdb(message):
    user_db = get_db('my_users')
    chat_id = message.chat.id
    id_ = get_id(message)
    if id_ is None:
        obj = {
            'chat_id': chat_id,
            'username': message.chat.username,
            'first_name': message.chat.first_name
        }
        user_db.append(obj)
        write_db('my_users', user_db)


@bot.callback_query_handler(func=lambda commands:True)
def inline(commands):
    del_filter(commands)
    if commands.data == 'menu':
        dies_help(commands.message)
    elif commands.data == 'Saosyant-Desatir':
        send_character_page(commands.message)
    evil_kings_btn(commands)
    music_btn(commands)
    gods_btn(commands)
    saosyant_btn(commands)
    my_userdb(commands.message)


bot.polling(none_stop=True, interval=0)