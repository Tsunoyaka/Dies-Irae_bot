from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaAudio
from get_db import get_album
from decouple import config
from math import ceil


bot = TeleBot(config('TOKEN'))


def special_btn(chat_id, page, db, name):
    pages = ceil(len(db)/10)
    keyboard = InlineKeyboardMarkup(row_width=pages)
    list_ = []
    for pg in range(pages):
        pg = InlineKeyboardButton(pg+1, callback_data=f"{name}:{pg+1}")
        list_.append(pg)
    keyboard.add(*list_)
    btn6 = InlineKeyboardButton('Назад к альбомам', callback_data='mus_back')
    keyboard.add(btn6)
    bot.send_message(chat_id, f'Вы находитесь на {page} странице', reply_markup=keyboard)


def group_media(chat_id, page, db):
    media = []
    for music in db[page*10-10:page*10]:
        media.append(InputMediaAudio(media=music))
    bot.send_media_group(chat_id, media=media)


def albums(message):
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Dies irae ~Acta est Fabula~ Original Soundtrack Neuen Welt Symphonie', callback_data='Fabula_Song')
    btn2 = InlineKeyboardButton('Dies irae ~Also sprach Zarathustra~ Main Theme & Image songs - Einsatz', callback_data='Zarathustra_Song')
    btn3 = InlineKeyboardButton('Dies irae ~Amantes amentes~ Ein Kleines Album', callback_data='Amantes_Song')
    btn4 = InlineKeyboardButton('Dies irae ~Interview with Kaziklu Bey~ - OST ｢Dominus tecum｣', callback_data='Bey_Song')
    btn5 = InlineKeyboardButton('Kajiri Kamui Kagura Shinza no Utage', callback_data='Kajiri_cong')
    btn6 = InlineKeyboardButton('В главное меню', callback_data='menu')
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(chat_id, 'Выберите альбом:', reply_markup=keyboard)


def fabula_song(message, page=1):
    db = get_album('Dies irae ~Acta est Fabula~ Original Soundtrack Neuen Welt Symphonie')
    chat_id = message.chat.id
    group_media(chat_id, page, db)
    special_btn(chat_id, page, db, 'fabula')


def zarathustra_song(message):
    db = get_album('Dies irae ~Also sprach Zarathustra~ Main Theme & Image songs - Einsatz')
    chat_id = message.chat.id
    media = []
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Назад к альбомам', callback_data='mus_back')
    keyboard.add(btn1)
    for music in db:
        media.append(InputMediaAudio(media=music))
    bot.send_media_group(chat_id, media=media)
    bot.send_message(chat_id, 'Послушать другие альбомы:', reply_markup=keyboard)


def amantes_song(message, page=1):
    db = get_album('Dies irae ~Amantes amentes~ Ein Kleines Album')
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Назад к альбомам', callback_data='mus_back')
    keyboard.add(btn1)
    group_media(chat_id, page, db)
    bot.send_message(chat_id, 'Послушать другие альбомы:', reply_markup=keyboard)


def bey_song(message, page=1):
    db = get_album('Dies irae ~Interview with Kaziklu Bey~ - OST ｢Dominus tecum｣')
    chat_id = message.chat.id
    group_media(chat_id, page, db)
    special_btn(chat_id, page, db, 'bey')


def kajiri_song(message, page=1):
    db = get_album('Kajiri Kamui Kagura Shinza no Utage')
    chat_id = message.chat.id
    group_media(chat_id, page, db)
    special_btn(chat_id, page, db, 'kajiri')


def del_funk(commands):
    try:
        for i in range(11):
            bot.delete_message(commands.message.chat.id, commands.message.message_id-i)
    except:
        None


def special_handler(commands):
    try:
        func = commands.data.split(':')[0]
        num = int(commands.data.split(':')[1])
        if func == 'fabula':
            fabula_song(commands.message, page=num)
        elif func == 'kajiri':
            kajiri_song(commands.message, page=num)
        elif func == 'bey':
            bey_song(commands.message, page=num)
        del_funk(commands)
    except IndexError:
        None


def music_btn(commands):
    print(commands)
    if commands.data == 'mus_back':
        albums(commands.message)
        del_funk(commands)
    elif commands.data == 'music':
        albums(commands.message)
    elif commands.data == 'Fabula_Song':
        fabula_song(commands.message)
    elif commands.data == 'Zarathustra_Song':
        zarathustra_song(commands.message)
    elif commands.data == 'Amantes_Song':
        amantes_song(commands.message)
    elif commands.data == 'Bey_Song':
        bey_song(commands.message)
    elif commands.data == 'Kajiri_cong':
        kajiri_song(commands.message)
    special_handler(commands)