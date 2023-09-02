import telebot
import requests
import random
from bs4 import BeautifulSoup


URL = 'https://www.yapokupayu.ru/blogs/post/100-yarkih-tsitat-iz-filmov-nad-kotorymi-stoit-zadumatsya-kazhdomu?ysclid=lly76urzru300205191'
token = '6358375438:AAGD6YAs3AiEBGHIcHdSgQJGXhu7jSxbfyg'
def parser(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('p')
    return [a.text for a in quotes]

list_of_quotes = parser(URL)
random.shuffle(list_of_quotes)

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Привет! Чтобы получить цитату, введи любую цифру:")
    
@bot.message_handler(content_types=['text'])
def quote(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_quotes[0])
        del list_of_quotes[0]
    else:
        bot.send_message(message.chat.id, 'Введи любую цифру:')

bot.infinity_polling(none_stop=True)