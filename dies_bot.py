from telebot import TeleBot
from telebot.types import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton
    )

from thron_gods import gods_btn, send_character_page, saosyant_btn
from evil_kings import evil_kings_btn
from ashavans import ashavans_btn
from get_db import (
    get_db,
    write_db,
    get_id,
    get_user,
    get_photo_evil_kings
)
from music import music_btn
from decouple import config


bot = TeleBot(config('TOKEN'))


@bot.message_handler(commands=['start'])
def welcome(message):
    dies_help(message)
    

@bot.message_handler(commands=['dies_help'])
def dies_help(message):
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Верховные Боги', callback_data='Divine')
    btn2 = InlineKeyboardButton('Первый божестенный престол', callback_data='first_heaven')
    btn3 = InlineKeyboardButton('Pantheon: Saosyant Desatir', callback_data='Saosyant-Desatir')
    btn4 = InlineKeyboardButton('Музыка', callback_data='music')
    btn5 = InlineKeyboardButton('Перейти к источнику', url='https://vk.com/dies_irae_light')
    btn6 = InlineKeyboardButton('Скрыть', callback_data='skip')
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(chat_id, 'Выберите нужный вам список:', reply_markup=keyboard)


@bot.message_handler(commands=['news'])
def dies_news(message):
    db = get_db('my_users')
    obj = """
*Обновление (◕‿◕✿)*

Что нового?
1. Список королей зла был перемещен в *Первый божественный престол*
2. Добавлены все доступные профили Ашаванов
3. Добавлены все доступные профили Друджвантов
4. Оптимизация бота (код был полностью переписан)

Если заметите ошибки или же у вас есть идеи и материалы для развития бота пишите cюда: @Tsunoyaka
    """
    photo = get_photo_evil_kings('news')
    admin = int(config('ADMIN'))
    if message.from_user.id == admin:
        for i in db:
            try:
                bot.send_photo(i['chat_id'], photo=photo, caption=obj, parse_mode='Markdown')
            except:
                None


def first_heaven(message):
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Короли Зла', callback_data='Evil_Kings')
    btn2 = InlineKeyboardButton('Ашаваны', callback_data='Ashavans')
    btn3 = InlineKeyboardButton('Друджванты', callback_data='Dragvant')
    btn4 = InlineKeyboardButton('В главное меню', callback_data='menu')
    keyboard.add(btn1, btn2, btn3, btn4)
    bot.send_message(chat_id, 'Выберите нужный вам список:', reply_markup=keyboard)


@bot.message_handler(commands=['bot_users'])
def bot_users(message):
    chat_id = message.chat.id
    admin = int(config('ADMIN'))
    if chat_id == admin:
        users = get_user()
        user_len = len(get_db('my_users'))
        bot.send_document(chat_id, document=users, visible_file_name='users.json', caption=f"Количество пользователей: {user_len}")
    else:
        bot.send_message(chat_id, 'Вы не имеете доступа к этой команде!')


def del_filter(commands):
    if not commands.data in ['Delete', 'fabula:1', 'fabula:2', 'fabula:3', 'fabula:4', 'fabula:5', 'mus_back', 
    'bey:1', 'bey:2', 'kajiri:1', 'kajiri:2', 'kajiri:3', 'kajiri:4']:
        bot.delete_message(commands.message.chat.id, commands.message.message_id)
    if commands.data == 'Delete':
        bot.delete_message(commands.message.chat.id, commands.message.message_id)


def my_userdb(message):
    user_db = get_db('my_users')
    chat_id = message.chat.id
    id_ = get_id(message)
    if id_ is None:
        obj = {
            'chat_id': chat_id,
            'username': message.chat.username
        }
        user_db.append(obj)
        write_db('my_users', user_db)


def first_heaven_filter(commands):
    if commands.data == 'first_heaven':
        first_heaven(commands.message)
    elif commands.data == 'Back_First_Heaven':
        first_heaven(commands.message)
    evil_kings_btn(commands)
    ashavans_btn(commands)


@bot.callback_query_handler(func=lambda commands:True)
def inline(commands):
    del_filter(commands)
    if commands.data == 'menu':
        dies_help(commands.message)
    if commands.data == 'Saosyant-Desatir':
        send_character_page(commands.message)
    music_btn(commands)
    gods_btn(commands)
    first_heaven_filter(commands)
    saosyant_btn(commands)
    my_userdb(commands.message)


bot.polling(none_stop=True, interval=0)