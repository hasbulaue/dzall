from telebot import TeleBot

token = '8417444268:AAEYy2ry9-jRTeTI6zGwovN1rK7p42weaoI'
bot = TeleBot(token)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет ответь на вопросы')
    bot.register_next_step_handler(message, ask_question)


def ask_question(message):
    bot.send_message (message.chat.id, 'Название какого языка программирования похоже на змею?')
    bot.register_next_step_handler(message, send_message)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == 'python' or message.text == 'Python' or message.text == 'питон' or message.text == 'Питон' or message.text == 'пайтон' or message.text == 'Пайтон':
        bot.send_message(message.chat.id, 'Верно')
        bot.register_next_step_handler(message, ask_question1)
    else:
        bot.send_message(message.chat.id, 'Попробуй снова')


def ask_question1(message):
    bot.send_message (message.chat.id, 'Напиши пайтон на английском языке')
    bot.register_next_step_handler(message, send_message1)


@bot.message_handler(content_types=['text'])
def send_message1(message):
    if message.text == 'python' or message.text == 'Python':
        bot.send_message(message.chat.id, 'Верно')
        bot.register_next_step_handler(message, ask_question2)
    else:
        bot.send_message(message.chat.id, 'Попробуй снова')


def ask_question2(message):
    bot.send_message (message.chat.id, 'Какой язык программирования лучше?')
    bot.register_next_step_handler(message, send_message2)


@bot.message_handler(content_types=['text'])
def send_message2(message):
    if message.text == 'python' or message.text == 'Python' or message.text == 'питон' or message.text == 'Питон' or message.text == 'пайтон' or message.text == 'Пайтон':
        bot.send_message(message.chat.id, 'Верно')
        bot.send_message(message.chat.id, 'Поздравляю! Вы ответили на все вопросы!')
    else:
        bot.send_message(message.chat.id, 'Попробуй снова')

bot.polling()