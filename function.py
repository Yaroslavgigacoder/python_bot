from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
bot = ApplicationBuilder().token("6152526442:AAFiHv3KmgbnkVhLxz9kXNh5GJzqfTqTMSQ").build()

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет!')
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f' {datetime.datetime.now().time()}')
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/time\n/help\n/music_list\n/serega\n')

async def music_list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/Travis_Scott__TakeWhatYouWant\n/Travis_Scott__SICKO_MODE\n')
async def travis_scott__takewhatyouwant_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('music/Post Malone, Ozzy Osbourne, Travis_Scott- Take What You Want.mp3', 'rb'))

async def travis_scott__sicko_mode_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('music/Travis Scott - SICKO MODE.mp3', 'rb'))
async def buetyful_men(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('photo/sergey.jpg', 'rb'))