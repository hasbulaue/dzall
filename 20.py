import telebot 


token = '8417444268:AAEYy2ry9-jRTeTI6zGwovN1rK7p42weaoI'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello, I am a bot. I can save your notes")
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, '/add_note --> Save your notes\n/get_note --> Get your saved notes\n/clear_all --> Clear all your saved notes')


@bot.message_handler(commands=['add_note'])
def add_note(message):
    note = message.text.replace('/add_note ', '')
    with open('notes.txt', 'a') as f:
        f.write(note + '\n')
    bot.reply_to(message, 'Note saved successfully')

@bot.message_handler(commands=['get_note'])
def get_note(message):
    with open('notes.txt', 'r') as f:
        notes = f.readlines()
    bot.reply_to(message, 'Your saved notes are:\n' + ''.join(notes))

@bot.message_handler(commands=['clear_all'])
def clear_all(message):
    with open('notes.txt', 'w') as f:
        f.write('')
    bot.reply_to(message, 'All your saved notes have been cleared')
                 

bot.polling()

