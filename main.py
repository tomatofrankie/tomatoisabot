import logging
import random
from datetime import datetime
import sched
from threading import Thread
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, User
from pytz import timezone
from alive import keep_alive

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
    \n/meal to choose a restaurant')


def echo(update, context):
    """Echo the user message."""
    echo = update.message.reply_text(update.message.text)
    print(timenow() + str(echo['chat']) +
    "\n" + str(echo['text']))
    

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

s = sched.scheduler(time.time, time.sleep)
def bg():
    timenow = datetime.now(timezone("Hongkong"))
    min = timenow.strftime("%M") 
    if min == "00" or min =="30":
        print(timenow)
    s.enter(1, 1, bg, ())

def run_thread():
    s.enter(1, 1, bg, ())
    s.run()

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5267877519:AAFOXQdhT-moRnscpniJU608gywutyfjl_4", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    thread = Thread(target=run_thread)
    thread.start()

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

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

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