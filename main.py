import logging
import random
from datetime import datetime
import sched
from threading import Thread
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from pytz import timezone
from alive import keep_alive
import yfinance as yf
import requests

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
keep_alive()

def timenow():
    time = datetime.now()
    time_log = time.strftime("%d-%m-%Y %H:%M:%S\n")
    return time_log

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    print(timenow() + "/start")
    update.message.reply_text('Hi! Try /help to find out more!')

def help(update, context):
    """Send a message when the command /help is issued."""
    print(timenow() + "/help")
    update.message.reply_text('Help menu:\n/start to start talking to the bot \
    \n/help to get the help menu\
    \n/time to get current time\
    \n/date to get today\'s date\
    \n/aboutme to know more about me\
    \n/meal to choose a restaurant\
    \n/hi to say hi to the bot\
    \n/usstock to check the stats of a stock')


# def echo(update, context):
#     """Echo the user message."""
#     echo = update.message.reply_text(update.message.text)
#     print(timenow() + str(echo['chat']) +
#     "\n" + str(echo['text']))
    

def gettime(update, context):
    """Show the time."""
    time = datetime.now(timezone("Hongkong"))
    gettime = time.strftime("%I:%M %p")
    print(timenow() + gettime)
    update.message.reply_text(gettime)

def date(update, context):
    """Show the time."""
    time = datetime.now(timezone("Hongkong"))
    date = time.strftime("%x")
    print(timenow() + date)
    update.message.reply_text(date)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def about(update, context):
    print(timenow() + "/about")
    update.message.reply_text("About Me:",
            reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('Youtube', url="https://www.youtube.com/c/番茄tomatofrankie")],
            [InlineKeyboardButton("Second Channel", url="https://www.youtube.com/channel/UCrlPId80vwGt70tDmaHdDeA")],
            [InlineKeyboardButton('Instagram', url="https://www.instagram.com/tomato.frankie/")],
            [InlineKeyboardButton("Facebook", url="https://www.facebook.com/tomatotofrankie")]
            ]))


cuisine = ["港式", "台灣菜", "中菜", "西式", "日式", "韓式", "印度、清真",
"泰國菜", "越南菜", "星馬菜", "cafe", "快餐", "咖喱", "酒吧", "素食", "其他"]

konglist = ["車仔麵", "茶記/冰室"]

chilist = ["米線", "火鍋", "雞煲", "酒樓、中菜館、點心", "餃子", "粥",
 "燒味", "四川菜", "北京菜", "上海菜", "潮州打冷", "刀削麵"]

westlist = ["義大利菜", "法國菜", "西班牙菜", "俄羅斯菜", "Burger",
 "Oyster", "Steak", "Pasta", "Pizza", "德國菜"]

japanlist = ["居酒屋", "壽司", "拉麵", "烏冬", "鐵板燒", "定食",
 "Omakase", "燒肉"]

korealist = ["韓燒", "炸雞", "韓式料理"]

otherlist = ["墨西哥菜", "土耳其菜", "印尼菜"]


def rand(update, context):
    print(timenow() + "/random")
    cuisine = ["港式", "台灣菜", "中菜", "西式", "日式", "韓式", "印度、清真",
    "泰國菜", "越南菜", "星馬菜", "cafe", "快餐", "咖喱", "酒吧", "素食", "其他"]
    choose(update, cuisine, konglist, chilist, westlist, japanlist, korealist, otherlist)

def choose(update, cuisine, konglist, chilist, westlist, japanlist, korealist, otherlist):
    choice = random.choice(cuisine)
    update.message.reply_text(choice)
    secondchoice = []
    print(choice)
    if choice == "港式": secondchoice = random.choice(konglist)
    if choice == "中菜": secondchoice = random.choice(chilist)
    if choice == "西式": secondchoice = random.choice(westlist)
    if choice == "日式": secondchoice = random.choice(japanlist)
    if choice == "韓式": secondchoice = random.choice(korealist)
    if choice == "其他": secondchoice = random.choice(otherlist)
    if secondchoice == []: pass
    else:
        update.message.reply_text(secondchoice)
        print(secondchoice)

def meal(update, context):
    print(timenow() + "/meal")
    update.message.reply_text("Cuisine list: 港式, 台灣菜, 中菜, 西式, \
    日式, 韓式, 印度、清真, 泰國菜, 越南菜, 星馬菜, cafe, 快餐, 咖喱, 酒吧, 素食, 其他\
    \n/random to randomly draw a cuisine without any restrictions\
    \n/remove_saved_1 to remove saved choices")

def remove_saved_1(update, context):
    cuisine.remove("酒吧")
    cuisine.remove("其他")
    chilist.remove("餃子")
    chilist.remove("粥")
    chilist.remove("上海菜")
    chilist.remove("潮州打冷")
    chilist.remove("刀削麵")
    westlist.remove("法國菜")
    westlist.remove("Oyster")
    westlist.remove("德國菜")
    westlist.remove("Steak")
    japanlist.remove("Omakase")
    korealist.remove("韓燒")
    print(timenow() + "/remove_saved_1")
    choose(update, cuisine, konglist, chilist, westlist, japanlist, korealist, otherlist)
    cuisine.extend(["酒吧","其他"])
    chilist.extend(["餃子","粥","上海菜","潮州打冷","刀削麵"])
    westlist.extend(["法國菜","Oyster","德國菜","Steak"])
    japanlist.extend(["Omakase"])
    korealist.extend(["韓燒"])

def loveyou(update, context):
    chat_id=update.effective_chat.id
    print(timenow() + "/loveyou0119")
    context.bot.send_document(chat_id,document=open('resources/foryou.zip', 'rb'), filename="foryou.zip")
    #context.bot.send_document(chat_id,document=open('resources/pic.png', 'rb'), filename="pic.png")
    #context.bot.send_document(chat_id,document=open('resources/readme.rtf', 'rb'), filename="readme.rtf")

s1 = sched.scheduler(time.time, time.sleep)
s2 = sched.scheduler(time.time, time.sleep)

def bg():
    timenow = datetime.now(timezone("Hongkong"))
    min = timenow.strftime("%M") 
    if min == "00" or min =="30":
        print("\n" + str(timenow) + "\n")
        time.sleep(60)
    s1.enter(1, 1, bg, ())

def run_thread1():
    s1.enter(1, 1, bg, ())
    s1.run()

def request():
    requests.get('https://tomatoisabot2.tomatofrankie1.repl.co')
    s2.enter(60, 2, request, ())

def run_thread2():
    s2.enter(1, 1, request, ())
    s2.run()

def usstock(update, context):
    print(timenow() + "/usstock")
    update.message.reply_text('Enter the ticker:\nEg. GME') 
    dp.add_handler(MessageHandler(Filters.text, check_price))
    
def check_price(update,context):  
    update.message.reply_text('Wait a second...') 
    ticker = update.message.text
    ticker = ticker.upper()
    print(ticker)
    try: 
        stock = yf.Ticker(ticker)
        stock_info = yf.Ticker(ticker).info
        market_price = stock_info['regularMarketPrice']
        previous_close_price = stock_info['regularMarketPreviousClose']
        print(market_price,previous_close_price)
    except:
        print('No such ticker.')
        update.message.reply_text('No such ticker.')
    else:
        try:
          ex_div_date = stock_info['exDividendDate']
          ex_div_date = datetime.fromtimestamp(ex_div_date)
        except:
          pass
        
        
        dividend = stock.dividends[-6:-1]
        day_Low = stock_info['dayLow']
        day_High = stock_info['dayHigh']
        pre_market_price = stock_info['preMarketPrice']
        news_list=stock.news

        print('market price: ', market_price)
        print('previous close price: ', previous_close_price)
        print('dividend rate: \n',dividend)
        print('ex-dividend date: ',ex_div_date)
        print('day low: ',day_Low)
        print('day high: ', day_High)
        print('pre-market price: ', pre_market_price)
        try:
            for news in range(3):
                news=news_list[news]
                title=news['title']
                link=news['link']
                print(title)
                print(link)
        except:
            print('No relevant news')
        
        update.message.reply_text(ticker + '\nmarket price: ' + str(market_price) +
        '\nprevious close price: ' + str(previous_close_price) + 
        '\ndividend rate:\n'+str(dividend)+
        '\nex-dividend date: ' + str(ex_div_date) +
        '\nday low: ' + str(day_Low) + 
        '\nday high: ' + str(day_High) + 
        '\npre-market price: '+ str(pre_market_price))
        try:
            for news in range(3):
                news=news_list[news]
                title=news['title']
                link=news['link']
                update.message.reply_text(title + '\n' + link)
        except:
            update.message.reply_text('No relevant news')
    return



# def usstock(update, context):
#     chat_id=update.effective_chat.id
#     print(timenow() + "/usstock")
#     update.message.reply_text('Input the command.\nEg. GME<180') 
#     dp.add_handler(MessageHandler(Filters.text, get_cmd))
#     #dp.add_handler(CommandHandler("end", end))
    
# def get_cmd(update, context):    
#     command = update.message.text
#     ticker = ''
#     price = ''
#     for char in command:
#         if char.isalpha():
#             ticker += char.upper()
#         if char.isdigit():
#             price += char
#     if '<' in command:
#         compare = '<'
#     if '>' in command:
#         compare = '>'
#     price = float(price)
#     Thread(target=run_thread2, args=(ticker,update,compare,price,)).start()

# def check_price(ticker,update,compare,price):
#     stock_info = yf.Ticker(ticker).info
#     market_price = stock_info['regularMarketPrice']
#     previous_close_price = stock_info['regularMarketPreviousClose']

#     update.message.reply_text(ticker + '\nmarket price: ' + str(market_price) + '\n' +
#     'previous close price: ' + str(previous_close_price))
#     print('market price: ', market_price)
#     print('previous close price: ', previous_close_price)
    
#     for i in range(1000):
#         stock_info = yf.Ticker(ticker).info
#         market_price = stock_info['regularMarketPrice']
#         previous_close_price = stock_info['regularMarketPreviousClose'] 
#         print(i)

#         if compare == '<':
#             if market_price < price:
#                 update.message.reply_text('alert!')
#                 print('alert!')
#                 return
#         if compare == '>':
#             if market_price > price:
#                 update.message.reply_text('alert!')
#                 print('alert!')
#                 return
        

# def run_thread2(ticker,update,compare,price):
#     s2.enter(5, 0, check_price, (ticker,update,compare,price))
#     s2.run()

def spam(update,context):
    print(timenow() + "/hi")
    random_number = int(100*random.random())
    print('"hi" x '+ str(random_number))
    for i in range(random_number):
        update.message.reply_text('hi')
    update.message.reply_text(str(random_number) + ' "hi"s had been sent')

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5267877519:AAFOXQdhT-moRnscpniJU608gywutyfjl_4", use_context=True)

    # Get the dispatcher to register handlers
    global dp
    dp = updater.dispatcher

    thread1 = Thread(target=run_thread1)
    thread1.start()
    thread2 = Thread(target=run_thread2)
    thread2.start()
    
    # on different commands - answer in Telegram
    print(timenow() + "start!")
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("time", gettime))
    dp.add_handler(CommandHandler("date", date))
    dp.add_handler(CommandHandler("aboutme", about))
    dp.add_handler(CommandHandler("meal", meal))
    dp.add_handler(CommandHandler("random", rand))
    dp.add_handler(CommandHandler("remove_saved_1", remove_saved_1))
    dp.add_handler(CommandHandler("loveyou0119", loveyou))
    dp.add_handler(CommandHandler("usstock",usstock))
    dp.add_handler(CommandHandler('hi',spam))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()