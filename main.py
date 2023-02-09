from function import *

print('server start')
bot.add_handler(CommandHandler("hi", hi_command))
bot.add_handler(CommandHandler("time", time_command))
bot.add_handler(CommandHandler("help", help_command))
bot.add_handler(CommandHandler("music_list", music_list_command))
bot.add_handler(CommandHandler("Travis_Scott__TakeWhatYouWant", travis_scott__takewhatyouwant_command))
bot.add_handler(CommandHandler("Travis_Scott__SICKO_MODE", travis_scott__sicko_mode_command))
bot.add_handler(CommandHandler("serega", buetyful_men))
bot.run_polling()