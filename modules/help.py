from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is the help message. List of commands:\n/start - Start the bot\n/help - Show this help message")

command_handler = CommandHandler('help', help_command)
