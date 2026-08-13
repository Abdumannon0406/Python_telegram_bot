import telegram

bot = telegram.Bot(token = "8794892081:AAFXck0imaaBYqiQ10V-rbERVuOBwjNJJJc")

offset = None 

while True:
    info = bot.getUpdates(offset = offset,timeout = 10)
    # print(info)

    for update in info:
        update_id = update.update_id

        offset = update_id+1

        if update.message and update.message.text:
            print(update.message.text)
            chat_id = update.message["chat"]["id"]

            text = update.message["text"]
            message_sent = bot.sendMessage(chat_id,text)