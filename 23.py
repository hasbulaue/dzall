import telebot
token = ''

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, i am a bot. I can save your messages ')

@bot.message_handler(commands = ['save_text'])
def save_message(message):
    bot.send_message(message.chat.id, 'Send me a message to save')
    bot.register_next_step_handler(message, save_text)
def save_text(message):
    with open('messages.txt', 'a', encoding = 'utf-8') as file:
        file.write(f'{message.chat.id}: {message.text}\n')
        bot.send_message(message.chat.id, 'Message saved')
@bot.message_handler(content_types=['photo'])
def save_photo(message):
    name = message.from_user.username
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('photos/' + name + '.jpg' , 'wb') as new_file:
        new_file.write(downloaded_file)
        bot.send_message(message.chat.id, 'Photo saved')

@bot.message_handler(content_types=['document'])
def save_document(message):
    name = message.from_user.username
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('documents/' + name, 'wb') as new_file:
        new_file.write(downloaded_file)
        bot.send_message(message.chat.id, 'Document saved')





@bot.message_handler(commands=['get_photo'])
def get_photo(message):
    name = message.from_user.username
    with open('photos/' + name + '.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
@bot.message_handler(commands = ['get_text'])
def get_text(message):
    for line in open('messages.txt', 'r', encoding = 'utf-8'):
        chat_id, text = line.strip().split(': ')
        if chat_id == str(message.chat.id):
            bot.send_message(message.chat.id, text)   
        else:
            None
        
bot.polling()