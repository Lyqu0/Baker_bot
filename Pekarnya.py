import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

TOKEN = "токен"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="заказать")],
            [types.KeyboardButton(text="информация")],
            [types.KeyboardButton(text="проблема с товаром")],
            [types.KeyboardButton(text="помощь")],
        ],
        resize_keyboard=True
    )

def get_ocenka_keyboard():
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="спасибо", callback_data="like"),
                types.InlineKeyboardButton(text="👎 Ну такое", callback_data="dislike")
            ],
            [
                types.InlineKeyboardButton(text="🌐 Наш сайт", url="https://google.com")
            ]
        ]
    )

@dp.callback_query(F.data == "like")
async def process_like(callback: types.CallbackQuery):
    await callback.answer("Спасибо за оценку! ❤️")
    await callback.message.edit_text("Вы выбрали: спасибо 👍")

@dp.callback_query(F.data == "dislike")
async def process_dislike(callback: types.CallbackQuery):
    await callback.answer("Спасибо за честный отзыв.")
    await callback.message.edit_text("Вы выбрали: не очень 👎")

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Выбери кнопку внизу 👇",
        reply_markup=get_main_keyboard()
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Привет! Я здесь, чтобы помочь вам выбрать товар")

@dp.message(lambda message: message.text == "заказать")
async def hello(message: types.Message):
    await message.answer(
        "Меню:\n- Булочка с маком\n- Булочка с повидлом\n- Круассан\n- Белый хлеб\n- Темный хлеб",
        reply_markup=get_ocenka_keyboard()
    )

@dp.message(lambda message: message.text == "информация")
async def roll_dice(message: types.Message):
    await message.answer("Я могу показать меню, принять фото для проверки товара и ответить на ваши вопросы.")

@dp.message(lambda message: message.text == "проблема с товаром")
async def foto(message: types.Message):
    await message.answer("Пришли мне фото, я его посмотрю 👀")

@dp.message(F.photo)
async def handle_photo(message: types.Message):
    await message.answer("Ого, крутая фотка! Сохранил себе 📸")

@dp.message(lambda message: message.text == "помощь")
async def pomoch(message: types.Message):
    await message.answer(
        "За помощью обращайтесь к @username",
        reply_markup=get_main_keyboard()
    )

@dp.message()
async def echo_message(message: types.Message):
    await message.answer("Пожалуйста, нажмите кнопку ниже или отправьте фото для проверки.", reply_markup=get_main_keyboard())

async def main_bot():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main_bot())
    