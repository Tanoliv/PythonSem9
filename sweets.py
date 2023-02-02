import telebot
from telebot import types
from random import randint

num_k_user=0
num_k_bot= 0

user_sweets = 0
bot_sweets= 0
sweets = 221

bot = telebot.TeleBot("6076494426:AAHH7kxcC58KQ6ee1jCseckcOG_5ZrkgyX0")


@bot.message_handler(commands=['игра']) # вызов функции по команде в списке
def controller(message):
    global sweets
    bot.send_message(message.chat.id, f"Введите количество не больше 28") # отправка сообщения (кому отправляем, что отправляем(str))
    bot.register_next_step_handler(message, user_input)
 
def bot_message(message):
    global sweets
    bot_sweets= randint(1,29)
    bot.send_message(message.chat.id, f"Беру:  {bot_sweets}, у меня заняты руки введите пожалуйста за меня") # отправка сообщения (кому отправляем, что отправляем(str))
    bot.register_next_step_handler(message, bot_input)
    #bot_input(message)

def get_count(message):
    global sweets 
    global num_k_user
    
    if sweets > 28: 
            sweets = sweets - user_sweets    
            num_k_user= num_k_user+ user_sweets
            bot.send_message(message.chat.id, f"Вы взяли {user_sweets} конфет, у вас {num_k_user} конфет, осталось {sweets}. Мой ход")
            bot_message(message)
    else:
        num_k_user=0
        sweets= 221
        bot.send_message(message.chat.id, f" УРА!!! Я выиграл!!! ОТДАЙ КОНФЕТЫ!!!")

def get_count2(message):    
    global sweets
    global num_k_bot
    
    if sweets > 28:    
            sweets = sweets - bot_sweets    
            num_k_bot= num_k_bot+ bot_sweets
            bot.send_message(message.chat.id, f"Я взял {bot_sweets} конфет, у меня {num_k_bot} конфет, осталось {sweets}. Ваш ход")
            controller(message)
    else: 
        num_k_bot=0 
        sweets= 221
        bot.send_message(message.chat.id, f"Ну да Вы выиграли. Если не стыдно возьмите мои конфеты")

 
def user_input(message):
    global user_sweets
    user_sweets = int(message.text)
    get_count(message)

def bot_input(message):
    global bot_sweets

    bot_sweets = int(message.text)    
    get_count2(message)
    

bot.infinity_polling()