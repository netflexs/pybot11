from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = "This is the help message. List of commands:\n/start - Start the bot\n/help - Show this help message"
    keyboard = [
        [InlineKeyboardButton("Back", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        # When the /help command is used
        await update.message.reply_text(help_text, reply_markup=reply_markup)
    elif update.callback_query:
        # When the callback query is used
        await update.callback_query.edit_message_text(help_text, reply_markup=reply_markup)
