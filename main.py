from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import config
import os
import importlib

# Initialize the bot
bot = ApplicationBuilder().token(config.API_TOKEN).build()

# Dynamically import all command modules from the 'modules' folder
# JADI DISINI FUNGSI UNTUK BACA SEMUA FILE YANG ADA DI DALAM FOLDER 'modules'
module_dir = 'modules'
for module in os.listdir(module_dir):
    if module.endswith('.py') and module != '__init__.py':
        module_name = module[:-3]
        command_module = importlib.import_module(f'{module_dir}.{module_name}')
        command_handler = getattr(command_module, 'command_handler', None)
        if command_handler:
            bot.add_handler(command_handler)
            

        callback_handler = getattr(command_module, 'callback_handler', None)
        if callback_handler:
            bot.add_handler(callback_handler)
if __name__ == '__main__':
    print("Bot is running...")
    bot.run_polling()
