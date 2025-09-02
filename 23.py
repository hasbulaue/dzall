from telebot import TeleBot
import requests
from bs4 import BeautifulSoup

token = '8417444268:AAEYy2ry9-jRTeTI6zGwovN1rK7p42weaoI'
bot = TeleBot(token)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello i can parsing your website\n",
                'Commands: /parse <url>\n',
                '/help - show this message\n')
    
@bot.message_handler(commands=['help'])
def help_message(message):
    return start_message(message)

@bot.message_handler(commands=['parse'])
def parse_message(message):
    bot.reply_to(message, "Please enter the URL to parse")
    bot.register_next_step_handler(message, parse_url)
def parse_url(message):
    url = message.text
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        description = soup.find('meta', attrs={'name': 'description'})['content']
        image = soup.find('meta', attrs={'property': 'og:image'})['content']
        bot.reply_to(message, f"Title: {title}\nDescription: {description}\nImage: {image}")
    except:
        bot.reply_to(message, "Error: Invalid URL")
bot.polling()