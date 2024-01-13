# 📺 watch Python Tutorial for this code on my YouTube:
# https://www.youtube.com/@serhiikolodych

# ✅ 1. TOKEN for your bot you can get from BotFather in Telegram: https://t.me/botfather
TOKEN = ""

# ✅ 2. Don't forget to install Aiogram 3.2 library, by typing in your terminal:
# pip install aiogram==3.2

import asyncio # is part of the Python standard library
from aiogram import Bot, Dispatcher, types # Bot - for send updates, Dispatcher - MUST_HAVE, types - MUST_HAVE
from aiogram.filters import CommandStart, Command # you can import only one of them (if needed)
from aiogram.types import FSInputFile  # to upload sticker file from the same file folder
import logging # if you want to get log prints in your console / terminal

# if you want to send updates and notifications to the user without the need for the user to message bot first.
bot = Bot(TOKEN)

# Create a Dispatcher for handling incoming messages and commands
dp = Dispatcher()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='logs_NAME.log')
logger = logging.getLogger('logs_NAME')

# Define a message handler for the /start command
@dp.message(CommandStart())
async def handle_start(message: types.Message):
    logger.info("--/START command pressed.")
    # Send a welcome message with the user's ID
    await message.answer(text=f"👋 user ID: {message.from_user.id}")


# Define a message handler for the /help command
@dp.message(Command("help"))
async def handle_help(message: types.Message):
    # Retrieve the user's ID
    chat_id = message.from_user.id
    # Send a message using bot.send_message method
    await bot.send_message(chat_id=chat_id, text=f"🙃 text")


# Define a message handler for the /stop command
@dp.message(Command("stop"))
async def handle_stop(message: types.Message):
    try:
        # Try to send a message indicating that the bot is not running
        await message.answer(f"🤔 Bot is not running.")
    except Exception as e:
        # If an error occurs during the attempt, send an error message
        await message.answer(f"😭 An error occurred: {e}")


# Define a message handler for any message that doesn't match the previous commands
@dp.message()
async def echo_message(message: types.Message):
    # Check if the message text is equal to 'sticker'
    if message.text.lower() == 'sticker':
        try:
            # sticker is from file your path ⬇️ ⬇️ ⬇️ to the file ending in "/.../*.tgs"
            sticker = FSInputFile("/Users/serhii/Desktop/bots/duck.tgs")
            await message.answer_sticker(sticker)
        except Exception as e:
            await message.answer(f"Failed to send sticker: {e}")
    # Else if the message text starts with ...
    elif message.text.lower().startswith('a'):
        # then send message
        await message.answer(f"✅ ok, no problem.")
    # Else not known text / command - send message
    else:
        await message.answer(f"🙋‍Didn't get that. /help")


# Define an asynchronous main function to start the bot
async def main():
    # print logs in console / terminal
    logging.basicConfig(level=logging.INFO)
    # Create a Bot instance with the specified token (needed to send messages without user's message)
    bot = Bot(token=TOKEN)
    # Start polling for updates using the Dispatcher
    await dp.start_polling(bot)


# Check if the script is being run directly
if __name__ == "__main__":
    # Run the main function using the asyncio.run() method
    asyncio.run(main())
