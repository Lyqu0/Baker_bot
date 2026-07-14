import telebot
import webbrowser

# Вместо 'ВАШ_ТОКЕН' нужно вставить реальный токен вашего бота от @BotFather
bot = telebot.TeleBot('8704114123:AAF59YRWDuyyw5K8fWNHxIssUQtj2ENTVg8')

# Обработка команд /start, /main или /hello
@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    # Отправляем приветствие с именем и фамилией пользователя
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')

# Обработка команды /help
@bot.message_handler(commands=['help'])
def help_info(message):
    # Отправка отформатированного сообщения с использованием HTML-тегов
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>Information</u></em>', parse_mode='html')

# Обработка команд /site или /website (открытие сайта в браузере на ПК, где запущен бот)
@bot.message_handler(commands=['site', 'website'])
def open_site(message):
    webbrowser.open('https://youtube.com')

# Обработка обычного текста (должна находиться в самом низу, перед запуском бота)
@bot.message_handler()
def info(message):
    # Приводим текст к нижнему регистру, чтобы проверка не зависела от регистра
    user_text = message.text.lower()
    
    if user_text == 'привет':
        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')
    elif user_text == 'id':
        # Отвечаем на конкретное сообщение пользователя (Reply), выводя его Telegram ID
        bot.reply_to(message, f'ID: {message.from_user.id}')

# Запуск бота на постоянное ожидание сообщений
bot.delete_webhook()  # удаляю webhook, чтобы избежать ошибки 409 (конфликт getUpdates)
bot.infinity_polling()