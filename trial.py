# import numpy

# def second_max(list):
#     if len(list) > 1:
#         max_number = max(list)
#         list.remove(max_number)
#         result = max(list)
#     else:
#         result = -1
#     return result

# #print(second_max([1,2,3,4,4]))

# def sum_of_list_of_list(list):
#     result = []
#     for i in list:
#         result.append(sum(i))
#     return result

# # print(sum_of_list_of_list([[],[2,6,4],[4,1,1]]))
# # print(sum_of_list_of_list([]))

# def average_of_list1(list):
#     mean = numpy.mean(list)
#     return mean

# def average_of_list2(list):
#     mean = sum(list) / len(list)
#     return mean

# # print(average_of_list1([2,6,1,6,7]))
# # print(average_of_list2([2,6,1,6,7]))

# def filter_list(list,number):
#     result = []
#     for i in list:
#         if len(i) > number:
#             result.append(i)
#     return result

# # print(filter_list(["happy", "fuck", "wtf", "professional"], 3))

# def check_common(list1,list2):
#     for a in list1:
#         for b in list2:
#             if a == b:
#                 return True
#             else:
#                 continue
#     return False
    
# # print(check_common([1,3,2],[2,7,8]))
# # print(check_common(['a', 'b'],['c','d']))

# def remove_item(list):
#     try:
#         del list[0]
#         del list[3:5]
#     except:
#         pass
#     return list 

# # print(remove_item([2,6,1,6,3,8,6,9]))
# import datetime

# def date_string(year,month,day,hour,minute):
#   date = datetime.datetime(year,month,day,hour,minute)
#   next_date = date + datetime.timedelta(days=1)
#   result = next_date.strftime("%d-%m-%Y:%H:%M")
#   return result

# print(date_string(2021,11,30,12,23))  

# def print_dict(dict,num):
#   result = 0
#   for key in dict:
#     if key > num:
#       result += dict[key]
#   return result

# dict = {1:3,2:5,6:4,8:2}
# print(print_dict(dict,6))

# print(list(reversed(range(1,11))))


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

