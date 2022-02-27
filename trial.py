# import datetime
# from pytz import timezone
# import sched, time
# from threading import Thread
# s = sched.scheduler(time.time, time.sleep)

# def bg():
#     timenow = datetime.datetime.now(timezone("Hongkong"))
#     min = timenow.strftime("%M") 
#     print(type(min))
#     if min == "04":
#         print(timenow)
#     s.enter(5, 1, bg, ())
# def run():    
#     s.enter(5, 1, bg, ())
#     s.run()
# thread = Thread(target = run)
# thread.start()

dict = {'date': 1645975803, 'delete_chat_photo': False, 'group_chat_created': False, 'message_id': 1031, 'new_chat_members': [], 'entities': [], 'channel_chat_created': False, 'photo': [], 'chat': {'type': 'private', 'username': 'tomatochop', 'first_name': '🍅🦊👶🏻', 'id': 869084943}, 'new_chat_photo': [], 'caption_entities': [], 'text': 'hi', 'supergroup_chat_created': False, 'from': {'id': 5267877519, 'first_name': 'tomatobot', 'username': 'tomatoisabot', 'is_bot': True}}
item = dict['chat']
print(dict["text"])