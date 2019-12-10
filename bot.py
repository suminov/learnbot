from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import setting
import ephem
import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO, filename='bot.log')



def greet_user(bot, update):
  greeting_text = 'Привет! Этот бот показывает то что ты написал. Так же через команду /planet вы можете узнать в каком созвездии находится планета'
  text = 'Вызван/start'
  logging.info(text)
  update.message.reply_text(greeting_text)


def talk_to_me(bot, update):
  user_text = 'Привет {}! Ты написал {}'.format(update.message.chat.first_name, update.message.text)
  logging.info(user_text)
  update.message.reply_text(user_text)

def planet_constellation(bot, update):
  a = update.message.text
  planet = a.split()
  date = str(datetime.date.today()).replace('-', '/')
  if getattr(ephem, planet[1]):
    planet_fun = getattr(ephem, planet[1])
    const = ephem.constellation(planet_fun(date))
    update.message.reply_text(const)
  



def main():
  mybot = Updater(setting.API_KEY, request_kwargs=setting.PROXY)

  dp = mybot.dispatcher
  dp.add_handler(CommandHandler('start', greet_user))
  dp.add_handler(CommandHandler('planet', planet_constellation))
  dp.add_handler(MessageHandler(Filters.text, talk_to_me))

  mybot.start_polling()
  mybot.idle()

main()