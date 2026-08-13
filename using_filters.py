from telegram.ext import CommandHandler, Updater,MessageHandler,CallbackContext,Filters
from telegram import Update



def text_sending(update: Update,context:CallbackContext):
    
    update.message.reply_text(update.message.text)
def photo_sending(update:Update,context:CallbackContext):
        

    file_id = update.message.photo[-1].file_id
    update.message.reply_photo(file_id)

def stiker_sending(update:Update,context: CallbackContext):
    update.message.reply_sticker(update.message.sticker)


updater = Updater(token="8794892081:AAFXck0imaaBYqiQ10V-rbERVuOBwjNJJJc")
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text,text_sending))
dispatcher.add_handler(MessageHandler(Filters.photo,photo_sending))
dispatcher.add_handler(MessageHandler(Filters.sticker,stiker_sending))

updater.start_polling()
updater.idle()