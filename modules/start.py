from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes
import importlib

# Import handler from modules.help
help_module = importlib.import_module('modules.help')
help_command_handler = getattr(help_module, 'help_command', None)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Help", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text("Hello! I am your bot. How can I help you today?", reply_markup=reply_markup)
    elif update.callback_query:
        # Edit the message for callback query context
        await update.callback_query.edit_message_text("Hello! I am your bot. How can I help you today?", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'help' and help_command_handler:
        # Call the help_command_handler function to show help
        await help_command_handler(update, context)
    elif query.data == 'back':
        # Return to the main menu
        await start(update, context)

command_handler = CommandHandler('start', start)
callback_handler = CallbackQueryHandler(button)

# Add the handlers to the application
# application.add_handler(command_handler)
# application.add_handler(callback_handler)
