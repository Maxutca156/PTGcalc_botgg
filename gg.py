import telebot
import math

bot = telebot.TeleBot('7439803388:AAG8d5m6Zc-uQrFqPpk2q6t3kqbbUnjP5vA')

line = ''
past_line = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('CE', callback_data='CE'),
             telebot.types.InlineKeyboardButton('x!', callback_data='x!'),
             telebot.types.InlineKeyboardButton('+/-', callback_data='+/-'),
             telebot.types.InlineKeyboardButton('<<<', callback_data='<<<'))

keyboard.row(telebot.types.InlineKeyboardButton('1/x', callback_data='1/x'),
             telebot.types.InlineKeyboardButton('x^2', callback_data='x^2'),
             telebot.types.InlineKeyboardButton('√x', callback_data='√x'),
             telebot.types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(telebot.types.InlineKeyboardButton('sinx', callback_data='sinx'),
             telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton('.', callback_data='.'),
             telebot.types.InlineKeyboardButton('=', callback_data='='))


@bot.message_handler(commands=['start'])
def send(message):
    global line
    if line == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, line, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def action(query):
    global line, past_line
    data = query.data

    if data == 'x!':
        line = str(math.factorial(int(float(line))))
    elif data == '√x':
        line = str(math.sqrt(float(line)))
    elif data == 'x^2':
        line = str(math.pow(float(line),(2)))
    elif data == '1/x':
        line = str(1 / float(line))
    elif data == 'sinx':
        line = str(math.sin(float(line)))
    elif data == 'CE':
        line = ''
    elif data == '<<<':
        if line != '':
            line = line[:-1]
    elif data == '+/-':
        if line.startswith(''):
            line = line[:1]
        else:
            line = '-' + line
    elif data == '=':
        try:
            line = str(float(eval(line)))
        except:
            line = 'На ноль делить нельзя!'
    else:
        line += data

    if (line != past_line and line != '') or ('0' != past_line and line == ''):
        if line == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=line, reply_markup=keyboard)

    if line == 'На ноль делить нельзя!':
        line = ''


bot.polling(none_stop=True)
