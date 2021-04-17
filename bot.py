# подключаем библиотеки
import requests
import random
from bs4 import BeautifulSoup
from datetime import date, timedelta

import telegram
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
# будем брать информацию за вчерашний день


def bot_telegram():
    count=0
    while count<3:
        yesterday = date.today() - timedelta(1)
        yesterday_str = yesterday.strftime('%d.%m.%Y')

        Fin = open ("page_id.txt" ) 
        str1 = Fin.readline().split()


        # На некоторых сайтах стоит минимальная защита и они не отдают контент без user-agent
        headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}
        # чтобы избежать кэширования на любом уровне, на всякий случай добавим случайно число
        url='https://habr.com/ru/post/'+(str1[0])+'/'
        r = requests.get(url)

        page_id1=float(str1[0])

        page_id2=str(page_id1+10)[0:len(str1)-3]
        fo = open("page_id.txt", "wt") 
        fo.write(page_id2)
        fo.close()
        # парсинг заголовков и времени создания новости
        soup = BeautifulSoup(r.text, 'html.parser')
        h2s = soup.find_all('span', class_='post__title-text')
        h2s = [x.text.strip() for x in h2s]
        #times = soup.find_all('span', class_='post__time')
        #times = [x.text.strip() for x in times]
        token=""
        #for k, t in enumerate(times):
                #if t.split()[0] == yesterday_str:  # если новость за вчера, то постим
                # Непосредственно здесь идет отправка. Инициализируем бота с помощью токена
        bot = telegram.Bot(token=token)
        chat_id = '@dessan_market'
    # тест новости
        if len(h2s)!=0:
            chat_text = 'Новая новость на <a href="'+format(url)+'">сайте</a>:\n <b>'+format(h2s[0])+'</b>'
            h2s.clear()
        # отправка поста в канал. Маленькая тонкость - используется HTML разметка
            # отправка поста в канал. Маленькая тонкость - используется HTML разметка
            bot.send_message(chat_id, text=chat_text, parse_mode=telegram.ParseMode.HTML)
            count+=1
        else:
            count-=1
if __name__ == "__main__":
    try:
        bot_telegram()
    except EOFError as er:
        print(er)