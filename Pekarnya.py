import asyncio # Берем библиотеку для асинхронных функций (способных ждать)
from aiogram import Bot, Dispatcher, types # Берем бота, диспетчер и типы из aiogram
from aiogram.filters.command import Command # Берем Command для /start, /help команд

TOKEN = '8704114123:AAF59YRWDuyyw5K8fWNHxIssUQtj2ENTVg8' # Дал токен бота (пароль для Telegram)

bot = Bot(token=TOKEN) # Создал бота с токеном - это ваш бот в Telegram
dp = Dispatcher() # Создал диспетчер - это "почтальон" для распределения сообщений

# ========== КОМАНДА /start ==========
@dp.message(Command("start")) # Слушатель: если пользователь напишет /start
async def main(message: types.Message): # Создал асинхронную функцию (может ждать)
    await bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name} что желаете заказать?') # Отправил приветствие

# ========== КОМАНДА /help ==========
@dp.message(Command("help")) # Слушатель: если пользователь напишет /help
async def help_info(message: types.Message): # Создал функцию для справки
    await bot.send_message(message.chat.id, '<b>Этот бот создан для заказа хлебо-булочных изделий</b>', parse_mode='html') # Отправил справку жирным текстом

# ========== КОМАНДА /site и /web ==========
@dp.message(Command("site")) # Слушатель: если пользователь напишет /site
@dp.message(Command("web")) # Слушатель: если пользователь напишет /web (обе команды = одна функция)
async def open_site(message: types.Message): # Создал функцию для отправки ссылки
    await bot.send_message(message.chat.id, 'Вот наш сайт: https://youtube.com 🌐') # Отправил ссылку пользователю


# ========== КОМАНДА /commands ==========
@dp.message(Command("commands")) # Слушатель: если пользователь напишет /commands
async def show_commands(message: types.Message): # Создал функцию для показа команд
    commands_text = '''📋 <b>Доступные команды:</b>

/start - Начать диалог с ботом 👋
/help - Справка о боте ℹ️
/site или /web - Открыть сайт 🌐
/commands - Показать все команды 📋''' # Создал текст со списком команд (три кавычки = много строк)
    await bot.send_message(message.chat.id, commands_text, parse_mode='html') # Отправил список команд

# ========== ОБРАБОТКА ОБЫЧНОГО ТЕКСТА ==========
@dp.message() # Слушатель: ловит ВСЕ сообщения которые не поймали другие функции
async def info(message: types.Message): # Создал функцию для обработки текста
    if message.text is None: # Проверка: есть ли текст? (может быть стикер, фото)
        return # Если нет текста - выходим из функции
    
    user_text = message.text.lower() # Взял текст и перевел в нижний регистр ("ХЛЕБ" → "хлеб")
    
    if 'хлеб' in user_text: # Проверка: если текст содержит "хлеб"
        await bot.send_message(message.chat.id, 'Отличный выбор! У нас есть белый и черный хлеб 🍞') # Отправил ответ про хлеб
    elif 'булка' in user_text: # Иначе если текст содержит "булка"
        await bot.send_message(message.chat.id, 'Булки свежие каждый день! 🥐') # Отправил ответ про булки
    elif 'пирог' in user_text: # Иначе если текст содержит "пирог"
        await bot.send_message(message.chat.id, 'Пироги с разными начинками! 🎂') # Отправил ответ про пироги
    else: # Иначе (ничего не совпало)
        await bot.send_message(message.chat.id, 'Извините, я вас не понял. Напишите, что вам нужно 😊') # Отправил: "не понял"

# ========== ЗАПУСК БОТА ==========
async def main_bot(): # Создал асинхронную функцию для запуска бота
    await dp.start_polling(bot) # Диспетчер слушает Telegram: "Есть ли новые сообщения?"

if __name__ == '__main__': # Проверка: это основной файл? (запустили напрямую)
    asyncio.run(main_bot()) # Запусти асинхронную функцию main_bot()
    