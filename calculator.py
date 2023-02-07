
import telebot
from telebot import types
import pandas as pd
import time as t

result= 0

def restart():
    global result
    result = 0
summ= 0
name= ''
res= 1
opr= ''

bot = telebot.TeleBot("6076494426:AAHH7kxcC58KQ6ee1jCseckcOG_5ZrkgyX0")


@bot.message_handler(commands = ['start_calc'])# декоратор для работы последующей функции
# свойство вызыающее функцию
def ssumma(message):
    global  result
   
    bot.send_message(message.chat.id, f'Привет! Вас приветствует мой калькулятор.')  
    mrk= telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1= telebot.types.KeyboardButton('Вычисление int(float) чисел')
    mrk.add(key1)
    bot.send_message(message.chat.id, f'Выбери ниже', reply_markup=mrk)    
 
@bot.message_handler(content_types= ['text'])
def int_float_calc(message):
    if message.text== 'Вычисление int(float) чисел':
        bot.send_message(message.chat.id, f'Введите числа  и оператор (+ или -, *, /, %, //, **) между числами  через пробел, для вычисления' ) 
        bot.register_next_step_handler(message, summa)
        bot.register_next_step_handler(message, opr2)

def calc_int(message):
    global result, summ 
    for i in summ:
        if i== '+':
            summ= [summ[i] for i in range(len(summ)) if summ[i]!='+' ]
            list= '+'.join(summ)
            print(list)
            result= eval(list)       
     
        elif i== '-':
                summ= [summ[i] for i in range(len(summ)) if summ[i]!='-' ]
                #print(summ)
                list= '-'.join(summ)
                print(list)
                result= eval(list)
                print('r-',result)

        elif i== '*':
            summ= [summ[i] for i in range(len(summ)) if summ[i]!='*' ]
            print(summ)
            result = 1
            for i in range(len(summ)):   
                summ[i]= int(summ[i])
                result*= summ[i]

        elif i== '/':
            summ= [summ[i] for i in range(len(summ)) if summ[i]!='/' ]
            print(summ)
            list= '/'.join(summ)
            print(list)
            result= eval(list)          

        elif i== '%':        
            for i in range(len(summ)):            
                    if i%2== 0:               
                        summ[i]= int(summ[i])                        
                        result= summ[0]% summ[i]                       

        elif i== '//':        
            for i in range(len(summ)):            
                    if i%2== 0:               
                        summ[i]= int(summ[i])                        
                        result= summ[0]// summ[i]                      

        elif i== '**':        
            for i in range(len(summ)):            
                    if i%2== 0:               
                        summ[i]= int(summ[i])                        
                        result= summ[0]** summ[i]                    
                        result= str(result)    
                                      
    bot.send_message(message.chat.id, str(result))

@bot.message_handler(content_types= ['text'])
def calc_nocalc(message):
    if message.text== 'Продолжить':
        restart()
        ssumma(message)

    elif message.text== 'Сохранить результат':        
        bot.send_message(message.chat.id, f'Введите фамилию оператора' ) 
        bot.register_next_step_handler(message, name1)

    elif message.text== 'Посмотреть журнал вычислений':
        filename= 'calc.csv'
        file= open(filename, 'r', encoding='UTF-8')
        file= file.read()    
        bot.send_message(message.chat.id, file )
        restart()
        res_book(message)

    else:
        exit()

def res_book(message):
    global name, opr, res, result
    calc_book= {
    'Дата/Время': [],
    'Фамилия': [],
    'Операция': [],
    'Результат': []
    }

    time= t.time()
    time_z= t.ctime(time)
    calc_book['Дата/Время'].append(time_z)

    name= name
    print('z имя', name)
    calc_book['Фамилия'].append(name)
   

    opr= opr
    print('z операция', opr)
    calc_book['Операция'].append(opr)

    res= result
    print('z результат', res)
    calc_book['Результат'].append(res)
    
    calc_book= calc_book

    cb= pd.DataFrame(data= calc_book)

    filename= 'calc.csv'
    file= open(filename, 'a', encoding='UTF-8')
    file.write(f'{cb}')
    bot.send_message(message.chat.id, f'Спасибо' )

    mrk= telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1= telebot.types.KeyboardButton('Продолжить')
    key2= telebot.types.KeyboardButton('Выход')
    key3= telebot.types.KeyboardButton('Сохранить результат')
    key4= telebot.types.KeyboardButton('Посмотреть журнал вычислений')
    mrk.add(key1)
    mrk.add(key2)
    mrk.add(key3)
    mrk.add(key4)
    bot.send_message(message.chat.id, f'Выбери', reply_markup=mrk)
    bot.register_next_step_handler(message, calc_nocalc)

def  name1(message):
    global name
    name= message.text
    print('фамилия',name)    
    res_book(message)     

def  opr2(message):
    global opr
    opr= message.text
    print('операция',opr)    
    res_book(message)  

def res1(message):
    global res
    res= message.text
    print('результат',res)    
    res_book(message)  

def  summa(message):
    global summ
    summ= list(map(str, message.text.split()))
    calc_int(message)

bot.infinity_polling() 
 