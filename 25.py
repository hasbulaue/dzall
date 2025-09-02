from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

token = '8417444268:AAEYy2ry9-jRTeTI6zGwovN1rK7p42weaoI'
bot = TeleBot(token)
button1 = InlineKeyboardMarkup()
button1.add(InlineKeyboardButton(text='Погода', callback_data='button1'))
button2 = InlineKeyboardMarkup()
button2.add(InlineKeyboardButton(text='Курс валют', callback_data='button2'))
button3 = InlineKeyboardMarkup()
button3.add(InlineKeyboardButton(text='Помощь', callback_data='button3'))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я бот, который поможет тебе узнать погоду, курс валют и другие важные вещи. Нажми на кнопку нужной тебе функции:', reply_markup=button1)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, 'Функция в разработке', reply_markup=button2)
    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, 'Текущий курс', reply_markup=button3)
    elif call.data == 'button3':
        bot.send_message(call.message.chat.id, 'Помощь')
bot.polling()

