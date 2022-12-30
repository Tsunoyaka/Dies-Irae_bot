import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaAudio
from get_db import get_album
from decouple import config


bot = telebot.TeleBot(config('TOKEN'))


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


def fabula_btn(message, page=1):
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=5)
    btn1 = InlineKeyboardButton('1', callback_data='one')
    btn2 = InlineKeyboardButton('2', callback_data='two')
    btn3 = InlineKeyboardButton('3', callback_data='three')
    btn4 = InlineKeyboardButton('4', callback_data='four')
    btn5 = InlineKeyboardButton('5', callback_data='five')
    btn6 = InlineKeyboardButton('Назад к альбомам', callback_data='mus_back')
    keyboard.add(btn1, btn2, btn3, btn4, btn5)
    keyboard.add(btn6)
    bot.send_message(chat_id, f'Вы находитесь на {page} странице', reply_markup=keyboard)


def bey_btn(message, page=1):
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=5)
    btn1 = InlineKeyboardButton('1', callback_data='one_bey')
    btn2 = InlineKeyboardButton('2', callback_data='two_bey')
    btn3 = InlineKeyboardButton('Назад к альбомам', callback_data='mus_back')
    keyboard.add(btn1, btn2)
    keyboard.add(btn3)
    bot.send_message(chat_id, f'Вы находитесь на {page} странице', reply_markup=keyboard)

def kajiri_btn(message, page=1):
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=5)
    btn1 = InlineKeyboardButton('1', callback_data='one_kajiri')
    btn2 = InlineKeyboardButton('2', callback_data='two_kajiri')
    btn3 = InlineKeyboardButton('3', callback_data='three_kajiri')
    btn4 = InlineKeyboardButton('4', callback_data='four_kajiri')
    btn6 = InlineKeyboardButton('Назад к альбомам', callback_data='mus_back')
    keyboard.add(btn1, btn2, btn3, btn4)
    keyboard.add(btn6)
    bot.send_message(chat_id, f'Вы находитесь на {page} странице', reply_markup=keyboard)


def fabula_song(message, page=1):
    db = get_album('Dies irae ~Acta est Fabula~ Original Soundtrack Neuen Welt Symphonie')
    chat_id = message.chat.id
    media = []
    if page == 1:
        for music in db[:10]:
            media.append(InputMediaAudio(media=music))
        bot.send_media_group(chat_id, media=media)
        fabula_btn(message, page)
    elif page == 2:
        for music in db[10:20]:
            media.append(InputMediaAudio(media=music))
        bot.send_media_group(chat_id, media=media)
        fabula_btn(message, page)
    elif page == 3:
        for music in db[20:30]:
            media.append(InputMediaAudio(media=music))
        bot.send_media_group(chat_id, media=media)
        fabula_btn(message, page)
    elif page == 4:
        for music in db[30:40]:
            media.append(InputMediaAudio(media=music))
        bot.send_media_group(chat_id, media=media)
        fabula_btn(message, page)
    elif page == 5:
        for music in db[40:50]:
            media.append(InputMediaAudio(media=music))
        bot.send_media_group(chat_id, media=media)
        fabula_btn(message, page)


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


def amantes_song(message):
    db = get_album('Dies irae ~Amantes amentes~ Ein Kleines Album')
    chat_id = message.chat.id
    media = []
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Назад к альбомам', callback_data='mus_back')
    keyboard.add(btn1)
    for music in db:
        media.append(InputMediaAudio(media=music))
    bot.send_media_group(chat_id, media=media)
    bot.send_message(chat_id, 'Послушать другие альбомы:', reply_markup=keyboard)


def bey_song(message, page=1):
    db = get_album('Dies irae ~Interview with Kaziklu Bey~ - OST ｢Dominus tecum｣')
    chat_id = message.chat.id
    media = []
    if page == 1:
        for music in db[:10]:
            media.append(InputMediaAudio(media=music))
        bot.send_media_group(chat_id, media=media)
        bey_btn(message, page)
    elif page == 2:
        for music in db[10:20]:
            media.append(InputMediaAudio(media=music))
        bot.send_media_group(chat_id, media=media)
        bey_btn(message, page)

def kajiri_song(message, page=1):
    db = get_album('Kajiri Kamui Kagura Shinza no Utage')
    chat_id = message.chat.id
    media = []
    if page == 1:
        for music in db[:10]:
            media.append(InputMediaAudio(media=music))
        bot.send_media_group(chat_id, media=media)
        kajiri_btn(message, page)
    elif page == 2:
        for music in db[10:20]:
            media.append(InputMediaAudio(media=music))
        bot.send_media_group(chat_id, media=media)
        kajiri_btn(message, page)
    elif page == 3:
        for music in db[20:30]:
            media.append(InputMediaAudio(media=music))
        bot.send_media_group(chat_id, media=media)
        kajiri_btn(message, page)
    elif page == 4:
        for music in db[30:40]:
            media.append(InputMediaAudio(media=music))
        bot.send_media_group(chat_id, media=media)
        kajiri_btn(message, page)


def del_funk(commands):
    try:
        for i in range(11):
            bot.delete_message(commands.message.chat.id, commands.message.message_id-i)
    except:
        None

def music_btn(commands):
    if commands.data == 'mus_back':
        del_funk(commands)
        albums(commands.message)
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
    elif commands.data == 'one':
        fabula_song(commands.message, page=1)
        del_funk(commands)
    elif commands.data == 'two':
        fabula_song(commands.message, page=2)
        del_funk(commands)
    elif commands.data == 'three':
        fabula_song(commands.message, page=3)
        del_funk(commands)
    elif commands.data == 'four':
        fabula_song(commands.message, page=4)
        del_funk(commands)
    elif commands.data == 'five':
        fabula_song(commands.message, page=5)
        del_funk(commands)
    elif commands.data == 'one_bey':
        bey_song(commands.message, page=1)
        del_funk(commands)
    elif commands.data == 'two_bey':
        bey_song(commands.message, page=2) 
        del_funk(commands)
    elif commands.data == 'one_kajiri':
        kajiri_song(commands.message, page=1) 
        del_funk(commands)
    elif commands.data == 'two_kajiri':
        kajiri_song(commands.message, page=2) 
        del_funk(commands)
    elif commands.data == 'three_kajiri':
        kajiri_song(commands.message, page=3)
        del_funk(commands)
    elif commands.data == 'four_kajiri':
        kajiri_song(commands.message, page=4) 
        del_funk(commands)
    elif commands.data == 'del':
        del_funk(commands)