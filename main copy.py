import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

from config import *
from sportmaster import *

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.delete_message(message.chat.id, message.message_id)  # Удаляем сообщение с командой /start
 
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
    phoneBtn = KeyboardButton(str_phoneBtn)
    nameBtn = KeyboardButton(str_nameBtn)
    carBtn = KeyboardButton(str_carBtn)
    markup.add(phoneBtn, nameBtn, carBtn)
    
    bot.send_message(message.chat.id, "Выберите варианты поиска: ", reply_markup=markup)

@bot.message_handler(content_types='text')
def bot_message(message):
    if message.text == str_phoneBtn:
        bot.send_message(message.chat.id, "Введите номер телефона:")

    elif message.text == "Назад":
        start(message)  # Возвращаемся к начальному меню
    else:
        receive_phone_number(message)


def receive_phone_number(msg):
    phone_number = validate_phone_number(msg.text)
    # Проверка правильности ввода номера
    if phone_number==None:
        bot.send_message(msg.chat.id, str_inputError)
        return
    infoFileName = "info_"+phone_number+".json"

    # Получаем информацию о телефоне
    info = {}

    phone_info = get_phone_info(phone_number)
    print("get_phone_info")
    info.update(phone_info)

    #доьбавить праивльную обработку номера
    sportmaster_info = search_in_sportmaster(phone_number[1:])
    print("search_in_sportmaster")
    if sportmaster_info is not None:
        info.update(sportmaster_info)

    write_dict_to_json(infoFileName, info)

    # Создаем новое меню с кнопкой "Назад" и закрепляем его
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
    backBtn = KeyboardButton("Назад")
    markup.add(backBtn)
    
    bot.send_message(msg.chat.id, "Выберите действие:", reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)