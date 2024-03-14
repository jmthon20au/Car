import requests
import telebot
from telebot.types import InlineKeyboardButton as Btn , InlineKeyboardMarkup as Mak
def car(info):
    
    url = "https://carnet.ai/recognize-url"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://carnet.ai',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    
    data = info
    
    response = requests.post(url,headers=headers, data=data)
    
    return response.json()
    
# @Crrazy_8 & @BRoK8
token = "6555471038:AAEjQZSjaiN_GF0V6eHWUzFkKew8sVXy6hg"
bot = telebot.TeleBot(token)
# @Crrazy_8 & @BRoK8

@bot.message_handler(commands=["start"])
def Start(message):
 bot.reply_to(message,'''👋🏻 اهلن بك عزيزي هذا البوت تم صنعه من الذكاء الاصطناعي بواسطة . @my00002 .

من هذا البوت يمكنك معرفة نوع السيارة بواسطة صورة السيارة .. 🛻''',reply_markup=Mak().add(Btn('More Bots',url="t.me/my00002")))

@bot.message_handler(content_types=['photo'])
def BMW(msg):
 file_id = msg.photo[-1].file_id
 file_info = bot.get_file(file_id)
 file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
 info = file_url
 xcar = car(info)
 if 'error' in xcar:
 	bot.reply_to(msg,'لم اتعرف على السيارة!')
 else:
 	carname = xcar['car']['make']
 	carmodel = xcar['car']['model']
 	years = xcar['car']['years']
 	angel = xcar['angle']['name']
 	color = xcar['color']['name']
 	xx = f'''تم التعرف على السيارة 🚧
. مصنع السيارة: {carname} .
. سنة اصدار السيارة: {years} .
. لون السيارة: {color} .
. زاوية تصوير السيارة : {angel} .
. اسم السيارة (موديلها) : {carmodel} .
⎯ ⎯ ⎯ ⎯'''
 	bot.reply_to(msg,xx)

bot.infinity_polling()