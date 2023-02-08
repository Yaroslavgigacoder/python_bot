from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from function import *


app = ApplicationBuilder().token("6152526442:AAFiHv3KmgbnkVhLxz9kXNh5GJzqfTqTMSQ").build()
print('server start')
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.run_polling()