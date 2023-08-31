import telebot
from config import keys, TOKEN
from utils import ConvertionException, Cnvrtor

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help (message: telebot.types.Message):
    text = 'Чтобы начать введи запрос по форме: \n <currency_1> <currency_2> <amount> \
\n Чтобы увидеть доступные валюты введите: /currency'
    bot.reply_to(message, text)

@bot.message_handler(commands=['currency'])
def currency (message: telebot.types.Message):
    text = 'Доступны к конвертации:'
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convrt(message: telebot.types.Message):
    try:
        currency = message.text.split(' ')
        if len(currency) != 3:
            raise ConvertionException('Ошибка при запросе!')

        quote, base, amount = currency
        total_base = Cnvrtor.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка в запросе.\n{e}')
    else:
        text = f'Сумма {amount} {quote} в {base} = {total_base} {base}'
        bot.send_message(message.chat.id, text)

bot.polling()
