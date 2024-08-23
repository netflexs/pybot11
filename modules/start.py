from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot. How can I help you today?")

command_handler = CommandHandler('start', start)
