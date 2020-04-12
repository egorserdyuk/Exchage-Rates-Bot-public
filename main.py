import telebot as tb
import parse as pe

token = 'token'

bot = tb.TeleBot(token)

"""" Testing unit handle
@bot.message_handler(content_types=["text"])
def test(message):
    bot.send_message(message.chat.id, message.text)
"""


# print(bot.get_me())


def logon(message):
    from datetime import datetime
    print("\n ~~~~~~~~")
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2})\n Текст: {3}".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text))


@bot.message_handler(commands=["start"])
def start_msg(message):
    bot.send_message(message.chat.id, "Доброе время суток, " + message.chat.first_name + '. Самые свежие курсы '
                                                                                         'интересующих тебя валют! '
                                                                                         'Что вас интересует? '
                                                                                         'Попробуйте ввести "USD" или '
                                                                                         '"/usd" для получения '
                                                                                         'актуального курса')
    logon(message)


# Handler'ы с протоколами обращений и запросами

@bot.message_handler(commands=["btc"])  # Bitcoin
def t_btc(message):
    bot.send_message(message.chat.id, "В разработке, извините")
    logon(message)


@bot.message_handler(commands=["usd"])  # United States Dollar
def t_usd(message):
    bot.send_message(message.chat.id, pe.usd() + " ₽")
    logon(message)


@bot.message_handler(commands=["eur"])  # Europian Union coin
def t_eur(message):
    bot.send_message(message.chat.id, pe.eur() + " ₽")
    logon(message)


@bot.message_handler(commands=["gbp"])  # Pound
def t_gbp(message):
    bot.send_message(message.chat.id, pe.gbp() + " ₽")
    logon(message)


@bot.message_handler(commands=["cny"])  # China uan
def t_cny(message):
    bot.send_message(message.chat.id, pe.cny() + " ₽")
    logon(message)


@bot.message_handler(commands=["jpy"])  # Japan uan
def t_jpy(message):
    bot.send_message(message.chat.id, pe.jpy() + " ₽")
    logon(message)


@bot.message_handler(commands=["chf"])  # dunno
def t_chf(message):
    bot.send_message(message.chat.id, pe.chf() + " ₽")
    logon(message)


@bot.message_handler(commands=["uah"])  # Ukranian hrivna
def t_uah(message):
    bot.send_message(message.chat.id, pe.uah() + " ₽")
    logon(message)


@bot.message_handler(commands=["byn"])  # dunno
def t_byn(message):
    bot.send_message(message.chat.id, pe.byn() + " ₽")
    logon(message)


@bot.message_handler(commands=["kzt"])  # Kazhakstan tenge
def t_kzt(message):
    bot.send_message(message.chat.id, pe.kzt() + " ₽")
    logon(message)


@bot.message_handler(content_types=['text'])
def currency(message):
    if message.text == "BTC":
        bot.send_message(message.chat.id, "В разработке, извините")
    elif message.text == "USD":
        bot.send_message(message.chat.id, pe.usd() + " ₽")
    elif message.text == "EUR":
        bot.send_message(message.chat.id, pe.eur() + " ₽")
    elif message.text == "GBP":
        bot.send_message(message.chat.id, pe.gbp() + " ₽")
    elif message.text == "CNY":
        bot.send_message(message.chat.id, pe.cny() + " ₽")
    elif message.text == "JPY":
        bot.send_message(message.chat.id, pe.jpy() + " ₽")
    elif message.text == "CHF":
        bot.send_message(message.chat.id, pe.chf() + " ₽")
    elif message.text == "UAH":
        bot.send_message(message.chat.id, pe.uah() + " ₽")
    elif message.text == "BYN":
        bot.send_message(message.chat.id, pe.byn() + " ₽")
    elif message.text == "KZT":
        bot.send_message(message.chat.id, pe.kzt() + " ₽")
    else:
        bot.send_message(message.chat.id, "Других валют пока не завезли, увы")
    logon(message)


if __name__ == "__main___":
    bot.polling(none_stop=True)
