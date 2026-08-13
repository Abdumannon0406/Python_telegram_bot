from telegram.ext import CommandHandler, Updater,MessageHandler,CallbackContext
from telegram import Update



def echo(update: Update,context:CallbackContext):
    
    # print(update)
    if update.message.text:
        update.message.reply_text(update.message.text)
    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        update.message.reply_photo(file_id)

    if update.message.sticker:
        update.message.reply_sticker(update.message.sticker)


updater = Updater(token="8794892081:AAFXck0imaaBYqiQ10V-rbERVuOBwjNJJJc")
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(filters=None,callback = echo))

updater.start_polling()
updater.idle()