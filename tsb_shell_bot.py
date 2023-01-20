from telegram.ext import *
import logging
import os
import pathlib
import json

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

BASE_DIR = pathlib.Path(__file__).resolve()
ROOT_DIR = os.path.dirname(BASE_DIR)
SECRETS_PATH = os.path.join(ROOT_DIR, 'secrets.json')  
SECRET_KEY = json.loads(open(SECRETS_PATH).read())

async def reboot_commmand(update, context):
    chat_id = update.effective_message.chat_id
    # try:
    #     due = float(context.args[0])
    #     if due < 0:
    #         await update.effective_message.reply_text("Sorry we can not go back to future!")
    #         return

    #     job_removed = remove_job_if_exists(str(chat_id), context)
    #     context.job_queue.run_once(alarm, due, chat_id=chat_id, name=str(chat_id), data=due)

    #     text = "Timer successfully set!"
    #     if job_removed:
    #         text += " Old one was removed."
    #     await update.effective_message.reply_text(text)

    # except (IndexError, ValueError):
    #     await update.effective_message.reply_text("Usage: /set <seconds>")
    await update.message.reply_text('Hello! Welcome To Store!')

if __name__ == '__main__':
    BOT_TOKEN = SECRET_KEY["BOT_TOKEN"]

    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('reboot', reboot_commmand))
    application.run_polling(1.0)