from telegram import InlineKeyboardMarkup,InlineKeyboardButton,Update
from telegram.ext import Updater, CallbackContext,CallbackQueryHandler,MessageHandler,Filters
import telegram,os,time
from pprint import pprint

updater = Updater(token = "8794892081:AAFXck0imaaBYqiQ10V-rbERVuOBwjNJJJc")

votes = {"likes": 0, "dislikes": 0, "voted_user":[]}


def start(update, context):
    key1  = InlineKeyboardButton(text= f'👍{votes['likes']}', callback_data= "reply1")
    key2 = InlineKeyboardButton(text=f'👎{votes['dislikes']}',callback_data="reply2")

    reply_markup = InlineKeyboardMarkup([[key1,key2]])
    update.message.reply_photo(open ("/mnt/data11/projects/Lessons/Python_telegram_bot/emotion_counting/image.png",'rb'),reply_markup = reply_markup)
    


def query(update,context):
    # pprint(update.callback_query)
    query = update.callback_query
    user_name = query.from_user.username
    user_id  = query.from_user.id
    print(user_id,user_name)
    data = query.data
    message = update.callback_query.message
    # pprint(data)
    time.sleep(1)
    
    if user_name in votes["voted_user"]:
        query.answer(text = "You have already voted")
        return
    
        # key1  = InlineKeyboardButton(text= '👍 1', callback_data= "reply1")
        # key2 = InlineKeyboardButton(text='👎 0',callback_data="reply2")

        # new_reply_markup = InlineKeyboardMarkup([[key1,key2]])

        # query.edit_message_reply_markup(reply_markup = new_reply_markup)
        # query.answer()
        # votes['likes']+=1
    if data =="reply1":
        votes["likes"]+=1

    if data =="reply2":
        votes["dislikes"]+=1
        # key1  = InlineKeyboardButton(text= '👍 0', callback_data= "reply1")
        # key2 = InlineKeyboardButton(text='👎 1',callback_data="reply2")

        # new_reply_markup = InlineKeyboardMarkup([[key1,key2]])

        # query.edit_message_reply_markup(reply_markup = new_reply_markup)
        # query.answer()


    key1  = InlineKeyboardButton(text= f'👍{votes['likes']}', callback_data= "reply1")
    key2 = InlineKeyboardButton(text=f'👎{votes['dislikes']}',callback_data="reply2")

    new_reply_markup = InlineKeyboardMarkup([[key1,key2]])

    query.edit_message_reply_markup(reply_markup = new_reply_markup)
    query.answer()
    votes["voted_user"].append(user_name)



    # query.answer(f'After 1 second delay. You have pressed {data} button')


dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(None,start))
dispatcher.add_handler(CallbackQueryHandler(query))

updater.start_polling()
updater.idle()