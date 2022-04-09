

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="tomato1017",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchone()

# print(myresult)

import sched
import time
import yfinance as yf
from threading import Thread
import pandas as pd
import datetime as dt


def check_price():
    command = input('Input the command: ')
    ticker = ''
    price = ''
    for char in command:
        if char.isalpha():
            ticker += char.upper()
        if char.isdigit():
            price += char
    if '<' in command:
        compare = '<'
    if '>' in command:
        compare = '>'
    
    price = float(price)
    stock = yf.Ticker(ticker)
    stock_info = yf.Ticker(ticker).info
    print(stock_info.keys())

    market_price = stock_info['regularMarketPrice']
    previous_close_price = stock_info['regularMarketPreviousClose']
    dividend = stock.dividends[-6:-1]
    ex_div_date = stock_info['exDividendDate']
    ex_div_date = dt.datetime.fromtimestamp(ex_div_date)
    day_Low = stock_info['dayLow']
    day_High = stock_info['dayHigh']
    pre_market_price = stock_info['preMarketPrice']
    
    print('market price: ', market_price)
    print('previous close price: ', previous_close_price)
    print('dividend rate: \n',dividend)
    print('ex-dividend date: ',ex_div_date)
    print('day low: ',day_Low)
    print('day high: ', day_High)
    print('pre-market price: ', pre_market_price)
    news_list=stock.news
    for news in range(len(news_list)):
        news=news_list[news]
        title=news['title']
        link=news['link']
        print(title)
        print(link)

    if compare == '<':
        if market_price < price:
            print('alert!')
            return
    if compare == '>':
        if market_price > price:
            print('alert!')
            return


# def run_thread():
#     s.enter(5, 0, check_price, ())
#     s.run()

#thread = Thread(target=run_thread)
#thread.start()


check_price()

# from pandas_datareader import data as pdr

# import yfinance as yf
# yf.pdr_override() # <== that's all it takes :-)

# # download dataframe
# data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
# print(data)

