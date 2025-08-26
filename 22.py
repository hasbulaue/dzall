import telebot
import time

token = '8417444268:AAEYy2ry9-jRTeTI6zGwovN1rK7p42weaoI'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, I am a bot! I can count the time between dates and hours.')

@bot.message_handler(commands=['help'])
def helps_message(message):
    bot.send_message(message.chat.id, '\n/start - start the bot, \n/help - show this message, ' \
    '\n/calc_time YYYY-MM-DD YYYY-MM-DD - calculate the time between two dates, ' \
    '\n/calc_hours HH:MM HH:MM - calculate the time between two hours, ' \
    '\n/now - time now, ' \
    '\n/days_until YYYY-MM-DD - calculate the number of days until the specified date')

@bot.message_handler(commands=['calc_time'])
def calc_time_message(message):
    try:
        date1 = message.text.split()[1]
        date2 = message.text.split()[2]
        date1_obj = time.strptime(date1, '%Y-%m-%d')
        date2_obj = time.strptime(date2, '%Y-%m-%d')
        time_diff = abs(time.mktime(date2_obj) - time.mktime(date1_obj))
        days = time_diff // (24 * 3600)
        bot.send_message(message.chat.id, f'The time between {date1} and {date2} is {days} days')
    except:
        bot.send_message(message.chat.id, 'Invalid input. Please enter the dates in the format YYYY-MM-DD.')
@bot.message_handler(commands=['calc_hours'])
def calc_hours(message):
    try:
        time1 = message.text.split()[1]
        time2 = message.text.split()[2]
        time1_obj = time.strptime(time1, '%H-%M')
        time2_obj = time.strptime(time2, '%H-%M')
        time_diff = abs(time.mktime(time2_obj) - time.mktime(time1_obj))
        hours = time_diff // 3600
        minutes = time_diff // 60
        bot.send_message(message.chat.id, f'The time between {time1} and {time2} is {hours} hours, {minutes} minutes')
    except:
        bot.send_message(message.chat.id, 'Invalid input. Please enter the times in the format HH:MM:SS.')

@bot.message_handler(commands=['now'])
def now_message(message):
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    bot.send_message(message.chat.id, f'The time now is {now}')

@bot.message_handler(commands=['days_until'])
def days_until_message(message):
    try:
        date = message.text.split()[1]
        date_obj = time.strptime(date, '%Y-%m-%d')
        days_diff = abs(time.mktime(date_obj) - time.time()) // (24 * 3600)
        bot.send_message(message.chat.id, f'There are {days_diff} days until {date}')
    except:
        bot.send_message(message.chat.id, 'Invalid input. Please enter the date in the format YYYY-MM-DD.')



bot.polling()