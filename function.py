from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет!')
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f' {datetime.datetime.now().time()}')
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/time\n/help\n')

