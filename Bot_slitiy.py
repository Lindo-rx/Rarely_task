import telebot
from telebot import types
bot = telebot.TeleBot('7959873800:AAH2pgOXXef0g6cm2fXLz54c38KZ-3TXb7E')
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Зарегистрироваться', )
    btn2 = types.KeyboardButton('Войти')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, 'Вас приветствует ITeam помощник!', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):

    if (message.text == 'Зарегистрироваться'):

        bot.send_message(message.chat.id, 'Сейчас тебя зарегистрируем! Введи своё имя:')
        bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введи свой пароль:')
    bot.register_next_step_handler(message, user_pass)
def user_pass(message):
    password = message.text.strip()
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован')
    bot.register_next_step_handler(message, answer)
def answer(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Посмотреть своё расписание")
    btn2 = types.KeyboardButton("Записаться на курс")
    btn3 = types.KeyboardButton("Информация по курсам")
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, text="Что хочешь сделать?", reply_markup=markup)
elif (message.text == 'Посмотреть своё расписание'):
        bot.send_message(message.chat.id, text="Всё ок")
    elif (message.text == 'Записаться на курс'):
            bot.send_message(message.chat.id, text="Всё ок")
    elif (message.text == 'Информация по курсам'):
            bot.send_message(message.chat.id, text="Всё ок")

    elif (message.text == 'Войти'):
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Посмотреть своё расписание")
        btn2 = types.KeyboardButton("Записаться на курс")
        btn3 = types.KeyboardButton("Информация по курсам")
        markup.row(btn1)
        markup.row(btn2, btn3)
        bot.send_message(message.chat.id, text="Что хочешь сделать?", reply_markup=markup)
    elif (message.text == 'Посмотреть своё расписание'):
        bot.send_message(message.chat.id, text="Всё ок")

    elif (message.text == 'Записаться на курс'):
        bot.send_message(message.chat.id, text="Всё ок")

    elif (message.text == 'Информация по курсам'):
        bot.send_message(message.chat.id, text="Всё ок")
bot.polling(none_stop=True)