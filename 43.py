import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Данные о тренерах
COACHES = {
    "иванов": {
        "name": "Иван Иванов",
        "specialization": "Силовые тренировки, кроссфит",
        "experience": "5 лет",
        "certificates": ["FPA", "ACE", "CrossFit L1"],
        "description": "Специализируется на силовых тренировках и функциональном тренинге."
    },
    "петрова": {
        "name": "Мария Петрова",
        "specialization": "Йога, пилатес, стретчинг",
        "experience": "7 лет",
        "certificates": ["Yoga Alliance", "Pilates Institute"],
        "description": "Эксперт в направлениях йоги и пилатеса."
    },
    "сидоров": {
        "name": "Алексей Сидоров",
        "specialization": "Бокс, ММА, функциональный тренинг",
        "experience": "8 лет",
        "certificates": ["Professional Boxing Coach", "MMA Trainer"],
        "description": "Тренер по единоборствам и функциональному тренингу."
    }
}

# Данные о групповых занятиях
GROUPS = {
    "йога": {
        "name": "Йога",
        "coach": "Мария Петрова",
        "duration": "60 минут",
        "level": "Все уровни",
        "description": "Классическая хатха йога для развития гибкости и силы.",
        "schedule": "Пн, Ср, Пт - 9:00, 19:00"
    },
    "пилатес": {
        "name": "Пилатес",
        "coach": "Мария Петрова", 
        "duration": "55 минут",
        "level": "Начинающие",
        "description": "Укрепление мышечного корсета и улучшение осанки.",
        "schedule": "Вт, Чт - 10:00, 18:00"
    },
    "бокс": {
        "name": "Бокс",
        "coach": "Алексей Сидоров",
        "duration": "75 минут", 
        "level": "Средний, Продвинутый",
        "description": "Техника ударов, работа в парах, функциональная подготовка.",
        "schedule": "Пн, Ср, Пт - 17:00, 20:00"
    },
    "кроссфит": {
        "name": "Кроссфит",
        "coach": "Иван Иванов",
        "duration": "60 минут",
        "level": "Все уровни",
        "description": "Высокоинтенсивные функциональные тренировки.",
        "schedule": "Пн-Пт - 7:00, 12:00, 18:00, 20:00"
    },
    "стретчинг": {
        "name": "Стретчинг",
        "coach": "Мария Петрова",
        "duration": "45 минут",
        "level": "Все уровни", 
        "description": "Растяжка для улучшения гибкости и расслабления.",
        "schedule": "Сб, Вс - 11:00, 17:00"
    }
}

# Расписание на неделю
WEEK_SCHEDULE = {
    "понедельник": {
        "9:00": "Йога (Мария Петрова)",
        "10:00": "Пилатес (Мария Петрова)",
        "17:00": "Бокс (Алексей Сидоров)", 
        "18:00": "Кроссфит (Иван Иванов)",
        "19:00": "Йога (Мария Петрова)",
        "20:00": "Бокс (Алексей Сидоров)"
    },
    "вторник": {
        "10:00": "Пилатес (Мария Петрова)",
        "12:00": "Кроссфит (Иван Иванов)",
        "18:00": "Пилатес (Мария Петрова)",
        "20:00": "Кроссфит (Иван Иванов)"
    },
    "среда": {
        "9:00": "Йога (Мария Петрова)",
        "12:00": "Кроссфит (Иван Иванов)", 
        "17:00": "Бокс (Алексей Сидоров)",
        "18:00": "Кроссфит (Иван Иванов)",
        "19:00": "Йога (Мария Петрова)",
        "20:00": "Бокс (Алексей Сидоров)"
    },
    "четверг": {
        "10:00": "Пилатес (Мария Петрова)",
        "12:00": "Кроссфит (Иван Иванов)",
        "18:00": "Пилатес (Мария Петрова)", 
        "20:00": "Кроссфит (Иван Иванов)"
    },
    "пятница": {
        "9:00": "Йога (Мария Петрова)",
        "12:00": "Кроссфит (Иван Иванов)",
        "17:00": "Бокс (Алексей Сидоров)",
        "18:00": "Кроссфит (Иван Иванов)",
        "19:00": "Йога (Мария Петрова)", 
        "20:00": "Бокс (Алексей Сидоров)"
    },
    "суббота": {
        "11:00": "Стретчинг (Мария Петрова)",
        "17:00": "Стретчинг (Мария Петрова)"
    },
    "воскресенье": {
        "11:00": "Стретчинг (Мария Петрова)",
        "17:00": "Стретчинг (Мария Петрова)"
    }
}

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    welcome_text = """
🏋️‍♂️ Добро пожаловать в фитнес-клуб "PowerFit"!

Доступные команды:
/coaches - Наши тренеры
/groups - Групповые занятия  
/today - Расписание на сегодня
/week - Расписание на неделю

Выберите команду для получения информации!
    """
    await update.message.reply_text(welcome_text)

# Команда /coaches
async def coaches(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Показывает список тренеров в виде кнопок"""
    keyboard = []
    for coach_key in COACHES.keys():
        coach_name = COACHES[coach_key]["name"].split()[1]  # Берем фамилию
        keyboard.append([InlineKeyboardButton(coach_name, callback_data=f"coach_{coach_key}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🏆 Наши тренеры:", reply_markup=reply_markup)

# Команда /groups  
async def groups(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Показывает список групповых занятий в виде кнопок"""
    keyboard = []
    for group_key in GROUPS.keys():
        group_name = GROUPS[group_key]["name"]
        keyboard.append([InlineKeyboardButton(group_name, callback_data=f"group_{group_key}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🧘‍♀️ Групповые занятия:", reply_markup=reply_markup)

# Команда /today
async def today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Показывает расписание на сегодня"""
    # В реальном приложении здесь должна быть логика определения текущего дня
    today_schedule = WEEK_SCHEDULE["понедельник"]
    
    schedule_text = "📅 Расписание на сегодня (понедельник):\n\n"
    for time, activity in today_schedule.items():
        schedule_text += f"🕒 {time}: {activity}\n"
    
    await update.message.reply_text(schedule_text)

# Команда /week
async def week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Показывает расписание на неделю"""
    schedule_text = "📅 Расписание на неделю:\n\n"
    
    for day, activities in WEEK_SCHEDULE.items():
        schedule_text += f"**{day.upper()}**\n"
        for time, activity in activities.items():
            schedule_text += f"🕒 {time}: {activity}\n"
        schedule_text += "\n"
    
    await update.message.reply_text(schedule_text)

# Обработчик нажатий на кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает нажатия на инлайн-кнопки"""
    query = update.callback_query
    await query.answer()
    
    callback_data = query.data
    
    if callback_data.startswith("coach_"):
        coach_key = callback_data.replace("coach_", "")
        coach = COACHES[coach_key]
        
        coach_info = f"""
👤 **Тренер: {coach['name']}**

🏅 Специализация: {coach['specialization']}
📅 Опыт работы: {coach['experience']}
📜 Сертификаты: {', '.join(coach['certificates'])}
📝 {coach['description']}
        """
        await query.edit_message_text(coach_info)
    
    elif callback_data.startswith("group_"):
        group_key = callback_data.replace("group_", "")
        group = GROUPS[group_key]
        
        group_info = f"""
🏃‍♀️ **Занятие: {group['name']}**

👤 Тренер: {group['coach']}
⏱ Длительность: {group['duration']}  
📊 Уровень: {group['level']}
📅 Расписание: {group['schedule']}
📝 {group['description']}
        """
        await query.edit_message_text(group_info)

# Основная функция
def main() -> None:
    """Запуск бота"""
    # Замените 'YOUR_BOT_TOKEN' на реальный токен вашего бота
    application = Application.builder().token("YOUR_BOT_TOKEN").build()
    
    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("coaches", coaches))
    application.add_handler(CommandHandler("groups", groups))
    application.add_handler(CommandHandler("today", today))
    application.add_handler(CommandHandler("week", week))
    
    # Добавляем обработчик нажатий на кнопки
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()