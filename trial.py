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

def print_dict(dict,num):
  result = 0
  for key in dict:
    if key > num:
      result += dict[key]
  return result

dict = {1:3,2:5,6:4,8:2}
print(print_dict(dict,6))






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