import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="order")],
            [types.KeyboardButton(text="information")],
            [types.KeyboardButton(text="product issue")],
            [types.KeyboardButton(text="help")],
        ],
        resize_keyboard=True
    )

def get_rating_keyboard():
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="thanks", callback_data="like"),
                types.InlineKeyboardButton(text="👎 Not great", callback_data="dislike")
            ],
            [
                types.InlineKeyboardButton(text="🌐 Our website", url="https://google.com")
            ]
        ]
    )

@dp.callback_query(F.data == "like")
async def process_like(callback: types.CallbackQuery):
    await callback.answer("Thanks for the rating! ❤️")
    await callback.message.edit_text("You chose: thanks 👍")

@dp.callback_query(F.data == "dislike")
async def process_dislike(callback: types.CallbackQuery):
    await callback.answer("Thanks for the honest feedback.")
    await callback.message.edit_text("You chose: not great 👎")

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Hi! Choose a button below 👇",
        reply_markup=get_main_keyboard()
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Hi! I'm here to help you choose a product.")

@dp.message(lambda message: message.text == "order")
async def order(message: types.Message):
    await message.answer(
        "Menu:\n- Poppy seed bun\n- Jam bun\n- Croissant\n- White bread\n- Dark bread",
        reply_markup=get_rating_keyboard()
    )

@dp.message(lambda message: message.text == "information")
async def information(message: types.Message):
    await message.answer("I can show the menu, accept a photo to check the product, and answer your questions.")

@dp.message(lambda message: message.text == "product issue")
async def product_issue(message: types.Message):
    await message.answer("Send me a photo, I'll take a look 👀")

@dp.message(F.photo)
async def handle_photo(message: types.Message):
    await message.answer("Wow, nice photo! Saved it 📸")

@dp.message(lambda message: message.text == "help")
async def help_text(message: types.Message):
    await message.answer(
        "For help, contact @username",
        reply_markup=get_main_keyboard()
    )

@dp.message()
async def echo_message(message: types.Message):
    await message.answer("Please press a button below or send a photo for review.", reply_markup=get_main_keyboard())

async def main_bot():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main_bot())
    