from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_to_echo = ' '.join(context.args)
    await update.message.reply_text(text_to_echo)

command_handler = CommandHandler('echo', echo)
