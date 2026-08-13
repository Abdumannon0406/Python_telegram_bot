from telegram.ext import CommandHandler, Updater,MessageHandler,CallbackContext,Filters
from telegram import Update
import re


def text_sending(update: Update,context:CallbackContext):
    
        update.message.reply_text(update.message.text)

def regex_sending(update:Update,context: CallbackContext):
    update.message.reply_text("Hello! How can I help you today?")
def bye_sending(update:Update, context: CallbackContext):
    update.message.reply_text("Goodbye! Have a great day!")

updater = Updater(token="8794892081:AAFXck0imaaBYqiQ10V-rbERVuOBwjNJJJc")
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r"hello",re.IGNORECASE)),regex_sending))
dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r"bye",re.IGNORECASE)),bye_sending))
dispatcher.add_handler(MessageHandler(Filters.text,text_sending))


updater.start_polling()
updater.idle()